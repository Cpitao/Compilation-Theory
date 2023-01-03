from __future__ import print_function
import AST


def addToClass(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func

    return decorator


class TreePrinter:

    @addToClass(AST.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.Instructions)
    def printTree(self, indent=0):
        self.children.printTree(indent)
        if self.instruction is not None:
            self.instruction.printTree(indent)

    @addToClass(AST.IntNum)
    def printTree(self, indent=0):
        print("| " * indent, self.value)

    @addToClass(AST.FloatNum)
    def printTree(self, indent=0):
        print("| " * indent, self.value)

    @addToClass(AST.Variable)
    def printTree(self, indent=0):
        print("| " * indent, self.name)

    @addToClass(AST.BinExpr)
    def printTree(self, indent=0):
        print("| " * indent, self.op)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.Transpose)
    def printTree(self, indent=0):
        print("| " * indent, "'")
        self.exp.printTree(indent + 1)

    @addToClass(AST.RelExpr)
    def printTree(self, indent=0):
        print("| " * indent, self.op)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.Assignment)
    def printTree(self, indent=0):
        print("| " * indent, self.op)
        self.assignable.printTree(indent + 1)
        self.exp.printTree(indent + 1)

    @addToClass(AST.If)
    def printTree(self, indent=0):
        print("| " * indent, "IF")
        self.exp.printTree(indent + 1)
        self.instruction.printTree(indent + 1)
        if self.elseInstruction is not None:
            self.elseInstruction.printTree(indent + 1)

    @addToClass(AST.While)
    def printTree(self, indent=0):
        print("| " * indent, "WHILE")
        self.exp.printTree(indent + 1)
        self.instruction.printTree(indent + 1)

    @addToClass(AST.For)
    def printTree(self, indent=0):
        print("| " * indent, "FOR")
        print("| " * (indent + 1), self.id)
        self.range.printTree(indent + 1)
        self.instruction.printTree(indent + 1)

    @addToClass(AST.Break)
    def printTree(self, indent=0):
        print("| " * indent, "BREAK")

    @addToClass(AST.Continue)
    def printTree(self, indent=0):
        print("| " * indent, "CONTINUE")

    @addToClass(AST.Return)
    def printTree(self, indent=0):
        print("| " * indent, "RETURN")
        self.exp.printTree(indent + 1)

    @addToClass(AST.Print)
    def printTree(self, indent=0):
        print("| " * indent, "PRINT")
        self.printable.printTree(indent + 1)

    @addToClass(AST.Printable)
    def printTree(self, indent=0):
        if type(self.value) is str:
            print("| " * indent, self.value)
        else:
            self.value.printTree(indent)
        if self.printable is not None:
            self.printable.printTree(indent)

    @addToClass(AST.ComplexInstruction)
    def printTree(self, indent=0):
        print("| " * indent, "COMPLEX INSTRUCTION")
        self.instruction.printTree(indent + 1)

    @addToClass(AST.MatrixAccess)
    def printTree(self, indent=0):
        print("| " * indent, "MATRIXACCESS")
        print("| " * (indent + 1), self.id)
        self.exp0.printTree(indent + 1)
        self.exp1.printTree(indent + 1)

    @addToClass(AST.Special)
    def printTree(self, indent=0):
        print("| " * indent, self.func)
        self.exp.printTree(indent + 1)

    @addToClass(AST.UMinus)
    def printTree(self, indent=0):
        print("| " * indent, "-")
        self.exp.printTree(indent + 1)

    @addToClass(AST.Matrix)
    def printTree(self, indent=0):
        print("| " * indent, "MATRIX")
        if self.body is not None:
            self.body.printTree(indent + 1)

    @addToClass(AST.MatrixBody)
    def printTree(self, indent=0):
        print("| " * indent, "VECTOR")
        self.vector.printTree(indent + 1)
        if self.next is not None:
            self.next.printTree(indent)

    @addToClass(AST.Vector)
    def printTree(self, indent=0):
        self.value.printTree(indent)
        if self.next is not None:
            self.next.printTree(indent)

    @addToClass(AST.Range)
    def printTree(self, indent=0):
        print("| " * indent, "RANGE")
        self.exp0.printTree(indent + 1)
        self.exp1.printTree(indent + 1)

    @addToClass(AST.Id)
    def printTree(self, indent=0):
        print("| " * indent, self.value)

    @addToClass(AST.Error)
    def printTree(self, indent=0):
        pass
