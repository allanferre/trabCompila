import ply.yacc as yacc
import ply.lex as lex

# Definição dos tokens
tokens = (
    'id', 'num',
    'def', 'int', 'print', 'return', 'if', 'else',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN',
    'LBRACE', 'RBRACE', 'COMMA', 'SEMICOLON',
    'LT', 'GT', 'EQ', 'NOTEQ',
)

# Regras de expressão regular para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_SEMICOLON = r';'
t_LT = r'<'
t_GT = r'>'
t_EQ = r'=='
t_NOTEQ = r'!='

def t_num(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_id(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

# Ignorar espaços em branco e tabs
t_ignore = ' \t'

# Tratamento de erro para caracteres não reconhecidos
def t_error(t):
    print(f"Caractere não reconhecido: '{t.value[0]}'")
    t.lexer.skip(1)

# Definição das regras da gramática
grammar = {
    'MAIN': [['STMT'], ['FLIST'], []],
    'FLIST': [['FDEF', 'FLIST'], ['FDEF']],
    'FDEF': [['def', 'id', '(', 'PARLIST', ')', '{', 'STMTLIST', '}']],
    'PARLIST': [['int', 'id', ',', 'PARLIST'], ['int', 'id'], []],
    'STMT': [['int', 'id', ';'], ['ATRIBST', ';'], ['PRINTST', ';'], ['RETURNST', ';'], ['IFSTMT'], ['{', 'STMTLIST', '}'], [';']],
    'ATRIBST': [['id', '=', 'EXPR'], ['id', '=', 'FCALL']],
    'FCALL': [['id', '(', 'PARLISTCALL', ')']],
    'PARLISTCALL': [['id', ',', 'PARLISTCALL'], ['id'], []],
    'PRINTST': [['print', 'EXPR']],
    'RETURNST': [['return']],
    'IFSTMT': [['if', '(', 'EXPR', ')', 'STMT', 'else', 'STMT'], ['if', '(', 'EXPR', ')', 'STMT']],
    'STMTLIST': [['STMT', 'STMTLIST'], ['STMT']],
    'EXPR': [['NUMEXPR', '<', 'NUMEXPR'], ['NUMEXPR', '>', 'NUMEXPR'], ['NUMEXPR', '==', 'NUMEXPR'], ['NUMEXPR']],
    'NUMEXPR': [['NUMEXPR', '+', 'TERM'], ['NUMEXPR', '-', 'TERM'], ['TERM']],
    'TERM': [['TERM', '*', 'FACTOR'], ['FACTOR']],
    'FACTOR': [['num'], ['(', 'NUMEXPR', ')'], ['id']]
}

# Lista de palavras reservadas
reserved = {
    'def': 'def', 'int': 'int', 'print': 'print', 'return': 'return', 'if': 'if', 'else': 'else'
}

# Definição das regras de produção
def p_MAIN(p):
    '''MAIN : STMT
            | FLIST
            |'''
    pass

def p_FLIST(p):
    '''FLIST : FDEF FLIST
             | FDEF'''
    pass

def p_FDEF(p):
    '''FDEF : def id LPAREN PARLIST RPAREN LBRACE STMTLIST RBRACE'''
    pass

def p_PARLIST(p):
    '''PARLIST : int id COMMA PARLIST
               | int id'''
    pass

def p_STMT(p):
    '''STMT : int id SEMICOLON
            | ATRIBST SEMICOLON
            | PRINTST SEMICOLON
            | RETURNST SEMICOLON
            | IFSTMT
            | LBRACE STMTLIST RBRACE
            | SEMICOLON'''
    pass

def p_ATRIBST(p):
    '''ATRIBST : id EQ EXPR
               | id EQ FCALL'''
    pass

def p_FCALL(p):
    '''FCALL : id LPAREN PARLISTCALL RPAREN'''
    pass

def p_PARLISTCALL(p):
    '''PARLISTCALL : id COMMA PARLISTCALL
                   | id'''
    pass

def p_PRINTST(p):
    '''PRINTST : print EXPR'''
    pass

def p_RETURNST(p):
    '''RETURNST : return'''
    pass

def p_IFSTMT(p):
    '''IFSTMT : if LPAREN EXPR RPAREN STMT else STMT
              | if LPAREN EXPR RPAREN STMT'''
    pass

def p_STMTLIST(p):
    '''STMTLIST : STMT STMTLIST
                | STMT'''
    pass

def p_EXPR(p):
    '''EXPR : NUMEXPR LT NUMEXPR
            | NUMEXPR GT NUMEXPR
            | NUMEXPR EQ NUMEXPR
            | NUMEXPR'''
    pass

def p_NUMEXPR(p):
    '''NUMEXPR : NUMEXPR PLUS TERM
               | NUMEXPR MINUS TERM
               | TERM'''
    pass

def p_TERM(p):
    '''TERM : TERM TIMES FACTOR
            | FACTOR'''
    pass

def p_FACTOR(p):
    '''FACTOR : num
              | LPAREN NUMEXPR RPAREN
              | id'''
    pass

# Tratamento de erros de sintaxe
def p_error(p):
    if p:
        print(f"Erro de sintaxe em '{p.value}' na linha {p.lineno}")
    else:
        print("Erro de sintaxe no final de entrada")

# Construção do analisador
parser = yacc.yacc()

# Exemplos de tokens
tokens1 = ['def', 'func', '(', 'int', 'var1', ',', 'int', 'var2', ')', '{', 'var1', '=', '5', ';', 'var2', '=', '3', ';', '}']
tokens2 = ['if', '(', 'var1', '<', 'var2', ')', '{', 'var1', '=', 'var2', ';', '}']
tokens3 = ['print', '(', 'var1', '+', 'var2', ')', ';']
tokens4 = ['return', ';']
tokens5 = ['func', '(', 'var1', ')', '{', 'var1', '=', '3', ';', '}']
tokens6 = ['int', 'var', '=', 'func', '(', 'var1', ')', ';']

# Testando os exemplos
examples = [tokens1, tokens2, tokens3, tokens4, tokens5, tokens6]
for i, tokens in enumerate(examples, 1):
    print(f"Exemplo {i}:")
    try:
        result = parser.parse(tokens)
        print("Pertence à gramática.")
    except Exception as e:
        print(f"Não pertence à gramática: {e}")

