class Node(object):
    pass


class Instructions(Node):
    def __init__(self, children, instruction=None):
        self.children = children
        self.instruction = instruction


class IntNum(Node):
    def __init__(self, value):
        self.value = value


class FloatNum(Node):

    def __init__(self, value):
        self.value = value


class Variable(Node):
    def __init__(self, name):
        self.name = name


class BinExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


class Transpose(Node):
    def __init__(self, exp):
        self.exp = exp


class RelExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


class Assignment(Node):
    def __init__(self, assignable, op, exp):
        self.assignable = assignable
        self.op = op
        self.exp = exp


class If(Node):
    def __init__(self, exp, instruction, elseInstruction=None):
        self.exp = exp
        self.instruction = instruction
        self.elseInstruction = elseInstruction


class While(Node):
    def __init__(self, exp, instruction):
        self.exp = exp
        self.instruction = instruction


class For(Node):
    def __init__(self, id, range, instruction):
        self.id = id
        self.range = range
        self.instruction = instruction


class Break(Node):
    pass


class Continue(Node):
    pass


class Return(Node):
    def __init__(self, exp=None):
        self.exp = exp


class Print(Node):
    def __init__(self, printable):
        self.printable = printable


class Printable(Node):
    def __init__(self, value, printable=None):
        self.value = value
        self.printable = printable


class ComplexInstruction(Node):
    def __init__(self, instruction):
        self.instruction = instruction


class MatrixAccess(Node):
    def __init__(self, id, exp0, exp1):
        self.id = id
        self.exp0 = exp0
        self.exp1 = exp1


class Special(Node):
    def __init__(self, func, exp):
        self.func = func
        self.exp = exp


class UMinus(Node):
    def __init__(self, exp):
        self.exp = exp


class Matrix(Node):
    def __init__(self, body=None):
        self.body = body


class MatrixBody(Node):
    def __init__(self, vector, next=None):
        self.vector = vector
        self.next = next


class Vector(Node):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Range(Node):
    def __init__(self, exp0, exp1):
        self.exp0 = exp0
        self.exp1 = exp1


class Id(Node):
    def __init__(self, value):
        self.value = value
# class Instructions(Node):
#     def __init__(self, instruction):
#         self.instruction = instruction
# ...
# fill out missing classes
# ...

class Error(Node):
    def __init__(self):
        pass
