from ply.lex import lex

# Palavras reservadas
reserved = {
    'def': 'DEF',
    'int': 'INT',
    'float': 'FLOAT',
    'string': 'STRING',
    'break': 'BREAK',
    'print': 'PRINT',
    'call': 'CALL',
    'read': 'READ',
    'return': 'RETURN',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'new': 'NEW',
    'null': 'NULL',
}

# Lista de tokens
tokens = [
    'IDENT',
    'FLOAT_CONSTANT',
    'INT_CONSTANT',
    'STRING_CONSTANT',
    'LPAREN',
    'RPAREN',
    'LCHAVES',
    'RCHAVES',
    'VIRGULA',
    'PONTO_VIRGULA',
    'LCOLCHETES',
    'RCOLCHETES',
    'ATRIBUICAO',
    'MENOR',
    'MENORIGUAL',
    'IGUAL',
    'DIFERENTE',
    'MAIOR',
    'MAIORIGUAL',
    'SOMA',
    'SUBTRACAO',
    'MULTIPLICACAO',
    'DIVISAO',
    'RESTO',
] + list(reserved.values())

# Regras de expressões regulares para tokens simples
t_ignore = ' \t'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCHAVES = r'\{'
t_RCHAVES = r'\}'
t_VIRGULA = r','
t_PONTO_VIRGULA = r';'
t_LCOLCHETES = r'\['
t_RCOLCHETES = r'\]'
t_ATRIBUICAO = r'='
t_MENOR = r'<'
t_MAIOR = r'>'
t_MENORIGUAL = r'<='
t_IGUAL = r'=='
t_DIFERENTE = r'!='
t_MAIORIGUAL = r'>='
t_SOMA = r'\+'
t_SUBTRACAO = r'-'
t_MULTIPLICACAO = r'\*'
t_DIVISAO = r'/'
t_RESTO = r'%'

# Regras de expressões regulares com ações
def t_IDENT(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENT')
    return t

def t_FLOAT_CONSTANT(t):
    r'\d+\.\d*|\d*\.\d+'
    t.value = float(t.value)
    return t

def t_INT_CONSTANT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING_CONSTANT(t):
    r'\".*?\"'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex()

def analyse_lex(data):
    lexer.input(data)
    tokens_list = []
    print('\nANÁLISE LÉXICA:\n')
    for tok in lexer:
        tokens_list.append(tok.type)
        print(tok)
    print('\nLista de Tokens:')
    print(tokens_list)

# Exemplo de entrada
data = '''
def func1 ( int A , int B )
{
int C = A + B ;
int D = B * C ;
return ;
}
def principal ()
{
int C ;
int D ;
int R ;
C = 4;
D = 5;
R = func1 (C , D );
return ;
}
'''

# Analisando o exemplo de entrada
analyse_lex(data)
