import scanner
import ply.yacc as yacc

tokens = scanner.tokens

precedence = (
    # to fill ...
    ("nonassoc", "IFPREC"),
    ("nonassoc", "ELSE"),
    ("nonassoc", "=", "ADDASSIGN", "SUBASSIGN", "MULASSIGN", "DIVASSIGN"),
    ("left", '+', '-'),
    ("left", "*", "/"),
    ("left", "'"),
    ("right", "UMINUS")
    # to fill ...
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(p):
    """program : instructions_opt"""


def p_instructions_opt_1(p):
    """instructions_opt : instructions """


def p_instructions_opt_2(p):
    """instructions_opt : """


def p_instructions_1(p):
    """instructions : instructions instruction """


def p_instructions_2(p):
    """instructions : instruction """


# since the rules below are already created and miss '{' and '}' block handling
# I just add this function here:
# def p_instructions_3(p):
#     """instructions : '{' instructions '}'
#                     | '{' instructions '}' instructions"""


def p_instruction(p):
    """instruction : expression
                    | assignment ';'
                    | ifexpr
                    | loop
                    | returnexpr ';'
                    | printexpr ';'
                    | BREAK ';'
                    | CONTINUE ';'
                    | complexinstruction"""


def p_complexinstruction(p):
    """complexinstruction : '{' instructions '}'"""


def p_assignment(p):
    """assignment : assignable '=' expression
                    | assignable ADDASSIGN expression
                    | assignable SUBASSIGN expression
                    | assignable MULASSIGN expression
                    | assignable DIVASSIGN expression"""


def p_assignable(p):
    """assignable : ID
                    | matrixelement"""


def p_matrixelement(p):
    """matrixelement : ID '[' expression ',' expression ']'"""


def p_expression(p):
    """expression : expression '+' expression
                    | expression '-' expression
                    | expression '*' expression
                    | expression '/' expression
                    | expression DOTADD expression
                    | expression DOTSUB expression
                    | expression DOTMUL expression
                    | expression DOTDIV expression
                    | expression LE expression
                    | expression GE expression
                    | expression EQ expression
                    | expression '>' expression
                    | expression '<' expression
                    | expression DIFF expression
                    | expression "'"
                    | INTNUM
                    | FLOATNUM
                    | assignable
                    | special '(' expression ')'
                    | '[' minit ']'
                    | '-' expression %prec UMINUS"""  # so that -1+2 doesn't become -(1+2)


def p_special(p):
    """special : EYE
                | ZEROS
                | ONES"""


def p_minit(p):
    """minit : minit ',' '[' matrixcontents ']'
                | '[' matrixcontents ']'"""


def p_matrixcontents(p):
    """matrixcontents : expression
                        | matrixcontents ',' expression"""


def p_ifexpr(p):
    """ifexpr : IF '(' expression ')' instruction %prec IFPREC
                | IF '(' expression ')' instruction ELSE instruction"""
    # here assume that if there is an if there must be instruction after it, same for else


def p_loop(p):
    """loop : forloop
            | whileloop"""


def p_forloop(p):
    """forloop : FOR ID '=' range instruction"""


def p_whileloop(p):
    """whileloop : WHILE '(' expression ')' instruction"""


def p_range(p):
    """range : expression ':' expression"""


def p_returnexpr(p):
    """returnexpr : RETURN expression"""


def p_printexpr(p):
    """printexpr : PRINT printable"""


def p_printable(p):
    """printable : STRING
                    | expression
                    | printable ',' expression"""


parser = yacc.yacc()
