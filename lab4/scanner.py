import ply.lex as lex

# Created automated tests using data from the lab in test.py

reserved = {'if': 'IF',
            'else': 'ELSE',
            'for': 'FOR',
            'while': 'WHILE',
            'break': 'BREAK',
            'continue': 'CONTINUE',
            'return': 'RETURN',
            'eye': 'EYE',
            'zeros': 'ZEROS',
            'ones': 'ONES',
            'print': 'PRINT'}

t_DOTADD = r"\.\+"
t_DOTSUB = r"\.-"
t_DOTMUL = r"\.\*"
t_DOTDIV = r"\./"
t_ADDASSIGN = r"\+="
t_SUBASSIGN = r"-="
t_MULASSIGN = r"\*="
t_DIVASSIGN = r"/="
t_LE = r"<="
t_GE = r">="
t_DIFF = r"!="
t_EQ = r"=="
t_STRING = r"\".*?\""
t_ignore = " \t"
t_ignore_COMMENT = r"\#.*"


def t_ID(t):
    r"[a-zA-Z_]+[a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, "ID")
    return t

def t_FLOATNUM(t):
    r"((0\.[0-9]*)|([1-9][0-9]*\.[0-9]*)|(\.[0-9]+))((E|e)[\+-]?[0-9]*)?"
    t.value = float(t.value)
    return t

def t_INTNUM(t):
    r"(0|([1-9][0-9]*))"
    t.value = int(t.value)
    return t

def t_newline(t):
    r"\n"
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)


tokens = ["DOTADD",
          "DOTSUB",
          "DOTMUL",
          "DOTDIV",
          "ADDASSIGN",
          "SUBASSIGN",
          "MULASSIGN",
          "DIVASSIGN",
          "LE",
          "GE",
          "DIFF",
          "EQ",
          "ID",
          "STRING",
          "INTNUM",
          "FLOATNUM"
          ] + list(reserved.values())
literals = "+-*/=<>()[]{}:',;"


lexer = lex.lex()