class Node(object):
    pass


class Instructions(Node):
    def __init__(self, children, instruction, line=None):
        self.children = children
        self.instruction = instruction
        self.line = line


class IntNum(Node):
    def __init__(self, value, line=None):
        self.value = value
        self.line = line


class FloatNum(Node):

    def __init__(self, value, line=None):
        self.value = value
        self.line = line


class Variable(Node):
    def __init__(self, name, line=None):
        self.name = name
        self.line = line


class BinExpr(Node):
    def __init__(self, op, left, right, line=None):
        self.op = op
        self.left = left
        self.right = right
        self.line = line


class Transpose(Node):
    def __init__(self, exp, line=None):
        self.exp = exp
        self.line = line


class RelExpr(Node):
    def __init__(self, op, left, right, line=None):
        self.op = op
        self.left = left
        self.right = right
        self.line = line


class Assignment(Node):
    def __init__(self, assignable, op, exp, line=None):
        self.assignable = assignable
        self.op = op
        self.exp = exp
        self.line = line


class If(Node):
    def __init__(self, exp, instruction, elseInstruction=None, line=None):
        self.exp = exp
        self.instruction = instruction
        self.elseInstruction = elseInstruction
        self.line = line


class While(Node):
    def __init__(self, exp, instruction, line=None):
        self.exp = exp
        self.instruction = instruction
        self.line = line


class For(Node):
    def __init__(self, id, range, instruction, line=None):
        self.id = id
        self.range = range
        self.instruction = instruction
        self.line = line


class Break(Node):
    def __init__(self, line=None):
        self.line = line


class Continue(Node):
    def __init__(self, line=None):
        self.line = line


class Return(Node):
    def __init__(self, exp=None, line=None):
        self.exp = exp
        self.line = line


class Print(Node):
    def __init__(self, printable, line=None):
        self.printable = printable
        self.line = line


class Printable(Node):
    def __init__(self, value, printable=None, line=None):
        self.value = value
        self.printable = printable
        self.line = line


class ComplexInstruction(Node):
    def __init__(self, instruction, line=None):
        self.instruction = instruction
        self.line = line


class MatrixAccess(Node):
    def __init__(self, id, exp0, exp1, line=None):
        self.id = id
        self.exp0 = exp0
        self.exp1 = exp1
        self.line = line


class Special(Node):
    def __init__(self, func, exp, line=None):
        self.func = func
        self.exp = exp
        self.line = line


class UMinus(Node):
    def __init__(self, exp, line=None):
        self.exp = exp
        self.line = line


class Matrix(Node):
    def __init__(self, body=None, line=None):
        self.body = body
        self.line = line


class MatrixBody(Node):
    def __init__(self, vector, next=None, line=None):
        self.vector = vector
        self.next = next
        self.line = line


class Vector(Node):
    def __init__(self, value, next=None, line=None):
        self.value = value
        self.next = next
        self.line = line


class Range(Node):
    def __init__(self, exp0, exp1, line=None):
        self.exp0 = exp0
        self.exp1 = exp1
        self.line = line


class Id(Node):
    def __init__(self, name, line=None):
        self.name = name
        self.line = line


# class Instructions(Node):
#     def __init__(self, instruction):
#         self.instruction = instruction
# ...
# fill out missing classes
# ...

class Error(Node):
    def __init__(self, line=None):
        self.line = line

