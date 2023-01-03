import scanner
import ply.yacc as yacc
import AST


tokens = scanner.tokens
ERRORED = False

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
        global ERRORED
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
        ERRORED = True
    else:
        print("Unexpected end of input")


def p_program(p):
    """program : instructions_opt"""
    p[0] = p[1]


def p_instructions_opt_1(p):
    """instructions_opt : instructions """
    p[0] = p[1]


def p_instructions_opt_2(p):
    """instructions_opt : """


def p_instructions_1(p):
    """instructions : instruction instructions"""
    p[0] = AST.Instructions(p[2], p[1], p.lineno(1))


def p_instructions_2(p):
    """instructions : instruction """
    p[0] = AST.Instructions(None, p[1], p.lineno(1))


def p_instruction(p):
    """instruction : expression
                    | assignment ';'
                    | ifexpr
                    | loop
                    | returnexpr ';'
                    | printexpr ';'
                    | breakOrContinue ';'
                    | complexinstruction"""
    p[0] = p[1]


def p_breakOrContinue(p):
    """breakOrContinue : brk
                        | cnt"""
    p[0] = p[1]


def p_brk(p):
    """brk : BREAK"""
    p[0] = AST.Break(p.lineno(1))


def p_cnt(p):
    """cnt : CONTINUE"""
    p[0] = AST.Continue(p.lineno(1))

def p_complexinstruction(p):
    """complexinstruction : '{' instructions '}'"""
    p[0] = AST.ComplexInstruction(p[2], p.lineno(1))


def p_assignment(p):
    """assignment : assignable '=' expression
                    | assignable ADDASSIGN expression
                    | assignable SUBASSIGN expression
                    | assignable MULASSIGN expression
                    | assignable DIVASSIGN expression
                    """
    p[0] = AST.Assignment(p[1], p[2], p[3], p.lineno(1))


def p_assignable(p):
    """assignable : ID
                    | ID '[' expression ',' expression ']'"""
    if len(p) > 2:
        p[0] = AST.MatrixAccess(p[1], p[3], p[5], p.lineno(1))
    else:
        p[0] = AST.Id(p[1], p.lineno(1))


def p_expression(p):
    """expression : binexp
                    | transpose
                    | num
                    | assignable
                    | special '(' expression ')'
                    | '[' minit ']'
                    | '-' expression %prec UMINUS"""  # so that -1+2 doesn't become -(1+2)
    if len(p) == 5:  # must be 'special'
        p[0] = AST.Special(p[1], p[3], p.lineno(1))
    elif len(p) == 4:
        p[0] = AST.Matrix(p[2], p.lineno(1))
    elif len(p) == 3:
        p[0] = AST.UMinus(p[2], p.lineno(1))
    else:
        p[0] = p[1]


def p_transpose(p):
    """transpose : expression "'"
    """
    p[0] = AST.Transpose(p[1], p.lineno(1))


def p_num(p):
    """num : int
            | float"""
    p[0] = p[1]


def p_int(p):
    """int : INTNUM"""
    p[0] = AST.IntNum(p[1], p.lineno(1))


def p_float(p):
    """float : FLOATNUM"""
    p[0] = AST.FloatNum(p[1], p.lineno(1))


def p_binexp(p):
    """binexp : mutexp
                | compexp"""
    p[0] = p[1]


def p_mutexp(p):
    """mutexp : expression '+' expression
                | expression '-' expression
                | expression '*' expression
                | expression '/' expression
                | expression DOTADD expression
                | expression DOTSUB expression
                | expression DOTMUL expression
                | expression DOTDIV expression"""
    p[0] = AST.BinExpr(p[2], p[1], p[3], p.lineno(1))


def p_compexp(p):
    """compexp : expression LE expression
                | expression GE expression
                | expression EQ expression
                | expression '>' expression
                | expression '<' expression
                | expression DIFF expression"""
    p[0] = AST.RelExpr(p[2], p[1], p[3], p.lineno(1))


def p_special(p):
    """special : EYE
                | ZEROS
                | ONES"""
    p[0] = p[1]


def p_minit(p):
    """minit : '[' matrixcontents ']' ',' minit
                | '[' matrixcontents ']'
                | matrixcontents"""
    if len(p) == 4:
        p[0] = AST.MatrixBody(p[2], None, p.lineno(1))
    elif len(p) == 2:
        p[0] = AST.MatrixBody(p[1], None, p.lineno(1))
    else:
        p[0] = AST.MatrixBody(p[2], p[5], p.lineno(1))


def p_matrixcontents(p):
    """matrixcontents : expression
                        |  expression ',' matrixcontents"""
    if len(p) > 2:
        p[0] = AST.Vector(p[1], p[3], p.lineno(1))
    else:
        p[0] = AST.Vector(p[1], None, p.lineno(1))


def p_ifexpr(p):
    """ifexpr : IF '(' expression ')' instruction %prec IFPREC
                | IF '(' expression ')' instruction ELSE instruction"""
    if len(p) < 7:
        p[0] = AST.If(p[3], p[5], line=p.lineno(1))
    else:
        p[0] = AST.If(p[3], p[5], p[7], line=p.lineno(1))


def p_loop(p):
    """loop : forloop
            | whileloop"""
    p[0] = p[1]


def p_forloop(p):
    """forloop : FOR ID '=' range instruction"""
    p[0] = AST.For(p[2], p[4], p[5], line=p.lineno(1))


def p_whileloop(p):
    """whileloop : WHILE '(' expression ')' instruction"""
    p[0] = AST.While(p[3], p[5], line=p.lineno(1))


def p_range(p):
    """range : expression ':' expression"""
    p[0] = AST.Range(p[1], p[3], line=p.lineno(1))


def p_returnexpr(p):
    """returnexpr : RETURN expression"""
    p[0] = AST.Return(p[2], line=p.lineno(1))


def p_printexpr(p):
    """printexpr : PRINT printable"""
    p[0] = AST.Print(p[2], line=p.lineno(1))


def p_printable(p):
    """printable : STRING
                | expression
                | printable ',' expression"""
    if len(p) == 2:
        p[0] = AST.Printable(p[1], line=p.lineno(1))
    else:
        p[0] = AST.Printable(p[3], p[1], line=p.lineno(1))


parser = yacc.yacc()
