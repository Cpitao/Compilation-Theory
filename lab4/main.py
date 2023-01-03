import sys
import ply.yacc as yacc
import Mparser
from TreePrinter import TreePrinter
import scanner


if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example1.m"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    mparser = Mparser.parser
    parser = yacc.yacc(module=Mparser)
    text = file.read()
    ast = parser.parse(text, lexer=scanner.lexer)
    if not Mparser.ERRORED:
        ast.printTree()
