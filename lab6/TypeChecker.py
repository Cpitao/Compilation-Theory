import AST
from collections import defaultdict
from SymbolTable import SymbolTable


ttype = defaultdict(lambda: defaultdict(lambda: defaultdict()))
binops = ['+', '-', '*', '/', '.+', '.-', '.*', './', '+=', '-=', '*=', '/=']
compops = ['>', '<', '==', '!=', '>=', '<=']
types = ["int", "float"]

for op in binops:
    for t1 in types:
        for t2 in types:
            ttype[op][t1][t2] = "float" if "float" == t1 or "float" == t2 else "int"

for op in compops:
    for t1 in types:
        for t2 in types:
            ttype[op][t1][t2] = "bool"

ttype['+']["string"]["string"] = "string"
ttype['*']["string"]["int"] = "string"  # allow python-like 'a'*5 = 'aaaaa'
for op in compops:
    ttype[op]["string"]["string"] = "bool"


class NodeVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):  # Called if no explicit visitor function exists for a node.
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.Node):
                            self.visit(item)
                elif isinstance(child, AST.Node):
                    self.visit(child)

    # simpler version of generic_visit, not so general
    # def generic_visit(self, node):
    #    for child in node.children:
    #        self.visit(child)


class SemanticError:

    error_msgs = {
        "incompatible_types_err": "Operation {} between {} and {} not allowed",
        "matrix_incompatible_shapes_op_err": "Operation not allowed between inconsistent matrix shapes {} and {}",
        "matrix_op_err": "Operation {} not supported for matrixes",
        "transpose_value_err": "Transposition for non-matrix type",
        "comparison_type_err": "Comparison not supported for non-scalar types",
        "break_err": "Break outside of loop",
        "continue_err": "Continue outside of loop",
        "undefined_reference_err": "Reference to undefined variable",
        "matrix_index_value_err": "Matrix indices must be integer",
        "index_out_of_range_err": "Index out of range ({})",
        "special_arg_type_err": "Special function's argument must be integer",
        "inconsistent_matrix_shape_err": "Matrix initialization with unequal row lengths",
        "range_type_err": "Range arguments must be integer"
    }

    def __init__(self, val, lineno, *args):
        self.val = val
        self.lineno = lineno
        self.args = args

    def __str__(self):
        return SemanticError.error_msgs[self.val].format(*self.args) + f" at line {self.lineno}"


class TypeChecker(NodeVisitor):

    def __init__(self):
        self.table = SymbolTable(None, "global")

    # def visit_BinExpr(self, node):
    #     # alternative usage,
    #     # requires definition of accept method in class Node
    #     type1 = self.visit(node.left)  # type1 = node.left.accept(self)
    #     type2 = self.visit(node.right)  # type2 = node.right.accept(self)
    #     op = node.op
    #
    # def visit_Variable(self, node):
    #     pass

    def visit_Instructions(self, node):
        if node.instruction is not None:
            self.visit(node.instruction)
        if node.children is not None:
            self.visit(node.children)

    def visit_IntNum(self, node):
        return "int"

    def visit_FloatNum(self, node):
        return "float"

    def visit_BinExpr(self, node):
        t1 = self.visit(node.left)
        t2 = self.visit(node.right)
        op = node.op

        if type(t1) is tuple and type(t2) is tuple:
            if op in ['.+', '.*', './', '.-']:
                if t1[1:] == t2[1:]:  # element-wise
                    if ttype[op][t1[0]][t2[0]] is not None:
                        return ttype[op][t1[0]][t2[0]], t1[1], t1[2]
                    print(SemanticError("incompatible_types_err", node.line, op, t1, t2))
                    return "undefined"
                else:
                    print(SemanticError("matrix_incompatible_shapes_op_err", node.line,
                                        f"({t1[1]}, {t1[2]})", f"({t2[1]}, {t2[2]})"))
                    return "undefined"
            elif op == '*':  # matrix multiplication
                if t1[2] == t2[1]:
                    if ttype[op][t1[0]][t2[0]] is not None:
                        return ttype[op][t1[0]][t2[0]], t1[1], t2[2]
                    print(SemanticError("incompatible_types_err", node.line, op, t1, t2))
                    return "undefined"
            else:
                print(SemanticError("matrix_op_err", node.line, op))
                return "undefined"
        elif type(t1) is not tuple and type(t2) is tuple:
            if op == '*':
                return ttype[op][t1][t2[0]], t2[1], t2[2]
            print(SemanticError("incompatible_types_err", node.line, op, t1, t2))
            return "undefined"
        elif type(t1) is tuple and type(t2) is not tuple:
            if op == '*':
                return ttype[op][t1[0]][t2], t1[1], t1[2]
            print(SemanticError("incompatible_types_err", node.line, op, t1, t2))
            return "undefined"
        elif type(t1) is not tuple and type(t2) is not tuple:
            return ttype[op][t1][t2]
        else:  # matrix op scalar
            print(SemanticError("incompatible_types_err", node.line, op, t1, t2))
            return "undefined"

    def visit_Transpose(self, node):
        t1 = self.visit(node.exp)
        if type(t1) is not tuple:
            print(SemanticError("transpose_value_err", node.line))
            return "undefined"

        return t1[0], t1[2], t1[1]  # will be (type, sizex, sizey)

    def visit_RelExpr(self, node):
        t1 = self.visit(node.left)
        t2 = self.visit(node.right)

        if t1 is not tuple and t2 is not tuple:
            return "bool"

        print(SemanticError("comparison_type_err", node.line))
        return "undefined"

    def visit_Assignment(self, node):
        # there are two cases here:
        # - assignment to matrix element
        # - assignment to ID
        t1 = self.visit(node.assignable)
        t2 = self.visit(node.exp)
        op = node.op
        if op == '=':
            if isinstance(node.assignable, AST.Id):
                self.table.put(node.assignable.name, t2)
        elif type(t1) is tuple and type(t2) is tuple:
            if op in ['+=', '-=']:  # no support for A /= B (like in numpy)
                if t1[1:] == t2[1:]:  # element-wise
                    if ttype[op][t1[0]][t2[0]] is not None:
                        return ttype[op[0]][t1[0]][t2[0]], t1[1], t1[2]
                    print(SemanticError("incompatible_types_err", node.line, op, t1, t2))
                    return "undefined"
                else:
                    print(SemanticError("matrix_incompatible_shapes_op_err", node.line,
                                        f"({t1[1]}, {t1[2]})", f"({t2[1]}, {t2[2]})"))
                    return "undefined"
            elif op == '*=':  # matrix multiplication
                if t1[2] == t2[1]:
                    if ttype[op[0]][t1[0]][t2[0]] is not None:
                        return ttype[op[0]][t1[0]][t2[0]], t1[1], t2[2]
                    print(SemanticError("incompatible_types_err", node.line, op, t1, t2))
                    return "undefined"
            else:
                print(SemanticError("matrix_op_err", node.line))
                return "undefined"
        elif type(t1) is tuple and type(t2) is not tuple:
            if op == '*=':
                self.table.put(node.assignable.name, (ttype[op[0]][t1[0]][t2[0]], t1[1], t1[2]))
                return ttype[op[0]][t1[0]][t2[0]], t1[1], t1[2]
        elif type(t1) is not tuple and type(t2) is not tuple:
            return ttype[op][t1][t2]
        else:  # matrix op scalar
            print(SemanticError("incompatible_types_err", node.line, op, t1, t2))
            return "undefined"

    def visit_If(self, node):
        self.visit(node.exp)
        self.table = self.table.pushScope("if")
        self.visit(node.instruction)
        self.table = self.table.getParentScope()
        if node.elseInstruction is not None:
            self.table.pushScope("else")
            self.visit(node.elseInstruction)
            self.table = self.table.getParentScope()

    def visit_While(self, node):
        self.visit(node.exp)
        self.table = self.table.pushScope("while")
        self.visit(node.instruction)
        self.table = self.table.getParentScope()

    def visit_For(self, node):
        self.table = self.table.pushScope("for")
        range_type = self.visit(node.range)

        self.table.put(node.id, range_type)
        self.visit(node.instruction)
        self.table = self.table.getParentScope()

    def visit_Break(self, node):
        scope = self.table
        while scope is not None:
            if scope.name not in ["while", "for"]:
                scope = scope.getParentScope()
            else:
                break
        if scope is None:
            print(SemanticError("break_err", node.line))

    def visit_Continue(self, node):
        scope = self.table
        while scope is not None:
            if scope.name not in ["while", "for"]:
                scope = scope.getParentScope()
            else:
                break
        if scope is None:
            print(SemanticError("continue_err", node.line))

    def visit_Return(self, node):
        self.visit(node.exp)

    def visit_Print(self, node):
        self.visit(node.printable)

    def visit_Printable(self, node):
        self.visit(node.value)
        if node.printable is not None:
            self.visit(node.printable)

    def visit_ComplexInstruction(self, node):
        self.table = self.table.pushScope("complexInstruction")
        self.visit(node.instruction)
        self.table = self.table.getParentScope()

    def visit_MatrixAccess(self, node):
        vtype = self.table.get(node.id)
        if vtype is None:
            print(SemanticError("undefined_reference_err", node.line))

        t1 = self.visit(node.exp0)
        t2 = self.visit(node.exp1)
        if t1 != "int" or t2 != "int":
            print(SemanticError("matrix_index_value_err", node.line))
        if not (0 < node.exp0.value < vtype[1]):
            print(SemanticError("index_out_of_range_err", node.line, node.exp0.value))
        if not (0 < node.exp1.value < vtype[2]):
            print(SemanticError("index_out_of_range_err", node.line, node.exp1.value))

        return vtype[0]

    def visit_Special(self, node):
        t1 = self.visit(node.exp)
        if t1 != "int":
            print(SemanticError("special_arg_type_err", node.line))
        return "int", node.exp.value, node.exp.value

    def visit_UMinus(self, node):
        self.visit(node.exp)

    def visit_Matrix(self, node):
        if node.body is not None:
            return self.visit(node.body)

    def visit_MatrixBody(self, node):
        t1 = self.visit(node.vector)
        if node.next is not None:
            t2 = self.visit(node.next)
            if t1[2] != t2[2]:
                print(SemanticError("inconsistent_matrix_shape_err", node.line))
                return "undefined"
            if t1[0] == "float" or t2[0] == "float":
                return "float", 1 + t2[1], t1[2]
            else:
                return "int", 1 + t2[1], t1[2]

        return t1[0], 1, t1[2]

    def visit_Vector(self, node):
        t1 = self.visit(node.value)
        if node.next is not None:
            t2 = self.visit(node.next)
            if t1 == "float" or t2[0] == "float":
                return "float", 1, 1 + t2[2]
            else:
                return "int", 1, 1 + t2[2]

        return t1, 1, 1

    def visit_Range(self, node):
        t1 = self.visit(node.exp0)
        t2 = self.visit(node.exp1)
        if t1 != "int" or t2 != "int":
            print(SemanticError("range_type_err", node.line))
        return "int"

    def visit_Id(self, node):
        return self.table.get(node.name)

    def visit_Str(self, node):
        return "string"