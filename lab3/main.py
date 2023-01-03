import sys
import ply.yacc as yacc
# from Mparser import Mparser
import Mparser  # import this rather than above, cause my parser is not OOP
from TreePrinter import TreePrinter
from TypeChecker import TypeChecker
import scanner


if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "init.m"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    parser = yacc.yacc(module=Mparser)
    text = file.read()

    ast = parser.parse(text, lexer=scanner.lexer)
    print(ast)
    # Below code shows how to use visitor
    typeChecker = TypeChecker()
    typeChecker.visit(ast)  # or alternatively ast.accept(typeChecker)
