import AST
import SymbolTable
from Memory import *
from Exceptions import  *
from visit import *
import sys

sys.setrecursionlimit(10000)


def multiplication(x, y):
    if isinstance(x, list): # type checker should detect if there are incorrect types
        if len(x[0]) != len(y): # check if sizes match for multiplication
            raise Exception("Multiplication of matrices with incompatible shapes")
        return [[sum(x[i][k] * y[l][j] for k in range(len(x[i])) for l in range(y)) for j in range(len(y[0]))
                 for i in range(len(x))]]
    else:
        return x*y


def matrix_op(x, y, op):
    if len(x) != len(y) or len(x[0]) != len(y[0]):
        raise Exception("Incompatible matrix shapes")
    if op == '.+':
        return matrix_add(x, y)
    elif op == '.-':
        return matrix_sub(x, y)
    elif op == '.*':
        return matrix_mul(x, y)
    elif op == './':
        return matrix_div(x, y)


def matrix_add(x, y):
    return [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]


def matrix_sub(x, y):
    return [[x[i][j] - y[i][j] for j in range(len(x[0]))] for i in range(len(x))]


def matrix_mul(x, y):
    return [[x[i][j] * y[i][j] for j in range(len(x[0]))] for i in range(len(x))]


def matrix_div(x, y):
    return [[x[i][j] / y[i][j] for j in range(len(x[0]))] for i in range(len(x))]


class Interpreter(object):

    def __init__(self):
        self.memory = MemoryStack(Memory("global"))
        self.fast_funcs = {
            "+": lambda x,y: x+y,
            "-": lambda x,y: x-y,
            "/": lambda x,y: x/y,
            "*": lambda x,y: multiplication(x, y),
            ".+": lambda x,y: matrix_op(x, y, ".+"),
            ".-": lambda x,y: matrix_op(x, y, ".-"),
            ".*": lambda x,y: matrix_op(x, y, ".*"),
            "./": lambda x,y: matrix_op(x, y, "./"),
            "==": lambda x,y: x == y,
            "!=": lambda x,y: x != y,
            ">=": lambda x,y: x >= y,
            "<=": lambda x,y: x <= y,
            "<": lambda x,y: x < y,
            ">": lambda x,y: x > y,
            "+=": lambda name,x: self.memory.get(name) + x,
            "-=": lambda name,x: self.memory.get(name) - x,
            "*=": lambda name,x: self.memory.get(name) * x,
            "/=": lambda name,x: self.memory.get(name) / x,
            "=": lambda name,x: x
        }

    @on('node')
    def visit(self, node):
        pass

    @when(AST.Instructions)
    def visit(self, node):
        self.visit(node.instruction)
        if node.children is not None:
            self.visit(node.children)

    @when(AST.BinExpr)
    def visit(self, node):
        r1 = self.visit(node.left)
        is_string = False
        r2 = self.visit(node.right)
        # if any of these is a string (meaning id), we need to resolve it's value
        if isinstance(r1, str) and '"' not in r1:
            r1 = self.memory.get(r1)
        elif isinstance(r1, str):
            r1 = r1[1:-1]
            is_string = True
        if isinstance(r2, str) and '"' not in r2:
            r2 = self.memory.get(r2)

        res = self.fast_funcs[node.op](r1, r2)
        if is_string:
            return '"' + res + '"'
        else:
            return res

    @when(AST.IntNum)
    def visit(self, node):
        return node.value

    @when(AST.FloatNum)
    def visit(self, node):
        return node.value

    @when(AST.Variable)
    def visit(self, node):
        return self.memory.get(node.name)

    @when(AST.Transpose)
    def visit(self, node):
        exp = self.visit(node.exp)
        transposed = []
        for i in range(len(exp[0])):
            transposed.append([exp[j][i] for j in range(len(exp))])

        return transposed

    @when(AST.RelExpr)
    def visit(self, node):
        r1 = self.visit(node.left)
        r2 = self.visit(node.right)
        # if any of these is a string (meaning id), we need to resolve it's value
        if isinstance(r1, str):
            r1 = self.memory.get(r1)
        if isinstance(r2, str):
            r2 = self.memory.get(r2)

        return self.fast_funcs[node.op](r1, r2)

    @when(AST.Assignment)
    def visit(self, node):
        assignable = self.visit(node.assignable)
        exp = self.visit(node.exp)
        if isinstance(exp, str):
            exp = self.memory.get(exp)
        if isinstance(node.assignable, AST.MatrixAccess):
            i1, i2 = self.visit(node.assignable.exp0), self.visit(node.assignable.exp1)
            mat = self.memory.get(node.assignable.id)
            if isinstance(i1, int) and isinstance(i2, int):
                m, n = len(mat), len(mat[0])
                if -m <= i1 < m and -n <= i2 < n:
                    mat[i1][i2] = self.fast_funcs[node.op[0]](mat[i1][i2], exp)
                else:
                    raise Exception(f"Indices {(i1, i2)} out of range for matrix of shape {(m, n)}")
            else:
                raise Exception("Matrix indices are not integers")
        else:
            self.memory.set(assignable, self.fast_funcs[node.op](assignable, exp))

    @when(AST.If)
    def visit(self, node):
        if self.visit(node.exp):
            self.visit(node.instruction)
        elif node.elseInstruction is not None:
            self.visit(node.elseInstruction)

    # simplistic while loop interpretation
    @when(AST.While)
    def visit(self, node):
        r = None
        while self.visit(node.exp):
            try:
                r = self.visit(node.instruction)
            except BreakException:
                break
            except ContinueException:
                continue
        return r

    @when(AST.For)
    def visit(self, node):
        self.memory.push(Memory("for"))
        start, stop = self.visit(node.range.exp0), self.visit(node.range.exp1)
        if isinstance(start, str):
            start = self.memory.get(start)
        if isinstance(stop, str):
            stop = self.memory.get(stop)
        name = node.id
        self.memory.insert(name, start)
        for i in range(start, stop):
            self.memory.set(name, i)
            try:
                self.visit(node.instruction)
            except BreakException:
                break
            except ContinueException:
                continue
        self.memory.pop()

    @when(AST.Break)
    def visit(self, node):
        raise BreakException()

    @when(AST.Continue)
    def visit(self, node):
        raise ContinueException()

    @when(AST.Return)
    def visit(self, node):
        raise ReturnValueException(self.visit(node.exp))

    @when(AST.Print)
    def visit(self, node):
        self.visit(node.printable)

    @when(AST.Printable)
    def visit(self, node):
        if node is not None:
            v = self.visit(node.value)
            if node.printable is not None:
                if isinstance(v, str) and '"' in v:
                    print(v[1:-1], end=' ')
                elif not isinstance(v, str):
                    print(v)
                else:
                    print(self.memory.get(v), end=' ')
                self.visit(node.printable)
            else:
                if isinstance(v, str) and '"' in v:
                    print(v[1:-1])
                elif not isinstance(v, str):
                    print(v)
                else:
                    print(self.memory.get(v))

    @when(AST.ComplexInstruction)
    def visit(self, node):
        self.memory.push(Memory("block"))
        try:
            self.visit(node.instruction)
        except BreakException:
            self.memory.pop()
            raise BreakException()
        except ContinueException:
            self.memory.pop()
            raise ContinueException()
        self.memory.pop()

    @when(AST.MatrixAccess)
    def visit(self, node):
        return self.memory.get(node.id)[self.visit(node.exp0)][self.visit(node.exp1)]
        # return self.memory.get(self.visit(node.id))[self.visit(node.exp0)][self.visit(node.exp1)]

    @when(AST.Special)
    def visit(self, node):
        val = self.visit(node.exp)
        if node.func == "zeros":
            return [[0 for _ in range(val)] for _ in range(val)]
        elif node.func == "ones":
            return [[1 for _ in range(val)] for _ in range(val)]
        elif node.func == "eye":
            return [[1 if i == j else 0 for i in range(val)] for j in range(val)]

    @when(AST.UMinus)
    def visit(self, node):
        v = self.visit(node.exp)
        new_v = v.copy()
        if isinstance(v, list):
            for i in range(len(v)):
                for j in range(len(v[0])):
                    new_v[i][j] *= -1
        return new_v

    @when(AST.Matrix)
    def visit(self, node):
        if node.body is not None:
            return self.visit(node.body)
        return [[]]

    @when(AST.MatrixBody)
    def visit(self, node):
        m = [self.visit(node.vector)]
        current_node = node
        while current_node.next is not None:
            current_node = current_node.next
            m.append(self.visit(current_node.vector))
        return m

    @when(AST.Vector)
    def visit(self, node):
        v = [self.visit(node.value)]
        current_node = node
        while current_node.next is not None:
            current_node = current_node.next
            v.append(self.visit(current_node.value))
        return v

    @when(AST.Id)
    def visit(self, node):
        return node.name

    @when(AST.Str)
    def visit(self, node):
        return node.value

    @when(AST.Error)
    def visit(self, node):
        raise Exception("Error encountered")
