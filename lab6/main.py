import sys
import ply.yacc as yacc
import Mparser
from TypeChecker import TypeChecker
import scanner
from Interpreter import Interpreter


if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "tests/triangle.m"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    parser = yacc.yacc(module=Mparser)
    text = file.read()

    ast = parser.parse(text, lexer=scanner.lexer)

    typeChecker = TypeChecker()
    typeChecker.visit(ast)

    # ast.accept(Interpreter())
    interpreter = Interpreter()
    interpreter.visit(ast)
