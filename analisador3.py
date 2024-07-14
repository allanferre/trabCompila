from lark import Lark, UnexpectedInput
import tabelaPreditiva

# Definindo a gramática
grammar = tabelaPreditiva
grammar1 = '''
    start: MAIN
    MAIN: STMT | FLIST | 
    FLIST: FDEF FLIST | FDEF
    FDEF: "def" "id" "(" PARLIST ")" "{" STMTLIST "}"
    PARLIST: "int" "id" "," PARLIST | "int" "id" | 
    STMT: "int" "id" ";" | ATRIBST ";" | PRINTST ";" | RETURNST ";" | IFSTMT | "{" STMTLIST "}" | ";"
    ATRIBST: "id" "=" EXPR | "id" "=" FCALL
    FCALL: "id" "(" PARLISTCALL ")"
    PARLISTCALL: "id" "," PARLISTCALL | "id" | 
    PRINTST: "print" EXPR
    RETURNST: "return"
    IFSTMT: "if" "(" EXPR ")" STMT "else" STMT | "if" "(" EXPR ")" STMT
    STMTLIST: STMT STMTLIST | STMT
    EXPR: NUMEXPR "<" NUMEXPR | NUMEXPR ">" NUMEXPR | NUMEXPR "==" NUMEXPR | NUMEXPR
    NUMEXPR: NUMEXPR "+" TERM | NUMEXPR "-" TERM | TERM
    TERM: TERM "*" FACTOR | FACTOR
    FACTOR: "num" | "(" NUMEXPR ")" | "id"
    %import common.WS
    %ignore WS
'''

# Criando o analisador sintático
parser = Lark(grammar, start='start')

# Definindo as listas de tokens
tokens1 = ["def", "id", "(", "int", "id", ")", "{", "int", "id", ";", "}"]
tokens2 = ["def", "("]

# Função para analisar uma lista de tokens
def parse_tokens(tokens):
    try:
        parser.parse(' '.join(tokens))
        print(f"A lista {tokens} pertence à gramática.")
    except UnexpectedInput as e:
        print(f"A lista {tokens} não pertence à gramática. Erro na posição {e.pos_in_stream}.")

# Analisando as listas de tokens
parse_tokens(tokens1)
parse_tokens(tokens2)
