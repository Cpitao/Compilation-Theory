class Node:
    pass


class Program(Node):
    def __init__(self, instructions_opt):
        self.children = [instructions_opt]


class Instructions(Node):
    def __init__(self, instruction):
        self.children = [instruction]


class Expression(Node):
    def __init__(self, **kwargs):
        # kwargs either have:
        # - expression0, expression1, operator
        # - expression0, unary operator
        # - value (INTNUM/FLOATNUM)
        # - assignable
        # - special, expression0
        # - minit (matrix initializer)
        # - uminus, expression

class For(Node):
    def __init__(self, id, range, instruction):
        self.id = id
        self.range = range
        self.instruction = instruction


class Break(Node):
    pass


class Continue(Node):
    pass
