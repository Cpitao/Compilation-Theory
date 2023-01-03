class VariableSymbol:

    def __init__(self, name, type):
        self.name = name
        self.type = type


class SymbolTable(object):

    def __init__(self, parent, name):  # parent scope and symbol table name
        self.parent = parent
        self.name = name
        self.table = {}

    def put(self, name, symbol):  # put variable symbol or fundef under <name> entry
        self.table[name] = symbol

    def get(self, name):  # get variable symbol or fundef from <name> entry
        if name in self.table:
            return self.table[name]

        if self.parent is not None:
            return self.parent.get(name)
        return None

    def getParentScope(self):
        return self.parent

    def pushScope(self, name):
        return SymbolTable(self, name)

    def popScope(self):
        r = self.parent
        del self
        return r