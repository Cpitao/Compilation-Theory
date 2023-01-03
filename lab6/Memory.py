class UndefinedVariableException(Exception):
    pass


class EmptyStackPopException(Exception):
    pass


class Memory:

    def __init__(self, name): # memory name
        self.name = name
        self.variables = {}

    def has_key(self, name):  # variable name
        return name in self.variables

    def get(self, name):         # gets from memory current value of variable <name>
        return self.variables[name]

    def put(self, name, value):  # puts into memory current value of variable <name>
        self.variables[name] = value


class MemoryStack:

    def __init__(self, memory=None): # initialize memory stack with memory <memory>
        self.memory = [memory] if memory is not None else []
        self.mem_size = len(self.memory)

    def get(self, name):             # gets from memory stack current value of variable <name>
        for i in range(self.mem_size-1, -1, -1):
            if self.memory[i].has_key(name):
                return self.memory[i].get(name)
        raise UndefinedVariableException(f"No variable named {name}")

    def insert(self, name, value): # inserts into memory stack variable <name> with value <value>
        self.memory[-1].put(name, value)

    def set(self, name, value): # sets variable <name> to value <value>
        for i in range(self.mem_size-1, -1, -1):
            if self.memory[i].has_key(name):
                self.memory[i].put(name, value)
                break
        else:
            self.memory[-1].put(name, value)

    def push(self, memory): # pushes memory <memory> onto the stack
        self.memory.append(memory)
        self.mem_size += 1

    def pop(self):          # pops the top memory from the stack
        if len(self.memory) == 0:
            raise EmptyStackPopException("Empty memory stack pop attempt")
        self.mem_size -= 1
        return self.memory.pop()
