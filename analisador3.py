from lark import Lark, UnexpectedInput
import tabelaPreditiva as tabela

def map_grammar_to_matrix(tabela):
    # Initialize an empty matrix
    matrix = []

    # Iterate over each row in the table
    for row in tabela:
        # Initialize an empty list for the current row in the matrix
        matrix_row = []

        # Iterate over each item in the row
        for item in row:
            # Append the item to the current row in the matrix
            matrix_row.append(item)

        # Append the current row to the matrix
        matrix.append(matrix_row)

    # Return the matrix
    return matrix

# Definindo a gramática
grammar = map_grammar_to_matrix(tabela)
grammar1 = '''		
[None,	None,	None,	None,	None,	None,	None,	"STMT",	None,	None,	None,	"STMT",	"FLIST", "STMT", None,	None,	"STMT",	"STMT",	"STMT",	"STMT",	None,	"",],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	"FDEF FLIST'",	None,	None,	None,	None,	None,	None,	None,	None,	None,],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	"FDEF",	None,	None,	None,	None,	None,	None,	None,	None,	"",	],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	"def ( PARLIST ) { STMLIST }",	None,	None,	None,	None,	None,	None,	None,	None,	None,],
[None,	None,	"",	    None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	"int id PARLIST'",	None,	None,	None,],
[None,	None,	"",	    None,	None,	", PARLIST",	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,],
[None,	None,	None,	None,	None,	None,	None,	";",	None,	None,	None,	"ATRIBST ;",	None,	"IFSTMT",	None,	None,	"PRINTST ;"	"RETURNST ;",	"int id",	"{ STMLIST' }",	None,	None,],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	"id = ATRIBST'",None,	None,	None,	None,	None,	None,	None,	None,	None,	None,],
[None,	"FACTOR TERM' NUMEXPR' EXPR'",	None,	None,	None,	None,	None,	None,	None,	None,	None,	"id TEST",	None,	None,	None,	"FACTOR TERM' NUMEXPR' EXPR'",	None,	None,	None,	None,	None,	None,],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	"print EXPR",	None,	None,	None,	None,	None,],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	"return",	None,	None,	None,	None,],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	"if ( EXPR ) STMT IFSTMT'",	None,	None,	None,	None,	None,	None,	None,	None,],
[None,	None,	None,	None,	None,	None,	None,	"",	    None,	None,	None,	"",	    None,	"",	["", "else"],	None,	"",	    "",	    "",	    "",	    "",	    "",	],
[None,	None,	None,	None,	None,	None,	None,	"STMT STMLIST'",None,	None,	None,	"STMT STMLIST'",	None,	"STMT STMLIST'",None,	None,	"STMT STMLIST'","STMT STMLIST'","STMT STMLIST'","STMT STMLIST'",None,None,],
[None,	None,	None,	None,	None,	None,	None,	"STMLIST",	    None,	None,	None,	"STMLIST",	None,	"STMLIST",	None,	None,	"STMLIST",	"STMLIST",	"STMLIST",	"STMLIST",	"",	None,],
[None,	"NUMEXPR EXPR'",None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	"NUMEXPR EXPR'",None,	None,	None,	None,	None,	None,],
["== NUMEXPR",	None,	"",	None,	None,	None,	None,	"",	"< NUMEXPR",	None,	"> NUMEXPR",	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,],
[None,	"TERM NUMEXPR'",	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	"TERM NUMEXPR'",	None,	None,	None,	None,	None,   None,],
["",	None,	"",	None,	"+ TERM NUMEXPR'",	None,	"- TERM NUMEXPR'",	"",	"",	None,	"",	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,],
[None,	"FACTOR TERM'",	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	"FACTOR TERM'",	None,	None,	None,	None,	None,None,],
["",	None,	"",	"* FACTOR TERM'",	"",	None,	"",	"",	"",	None,	"",	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,],
[None,	"( NUMEXPR )",	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	"num",	None,	None,	None,	None,	None,	None,],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	"id ( PARLISTCALL )",	None,	None,	None,	None,	None,	None,	None,	None,	None,   None,],
["TERM' NUMEXPR' EXPR'",	"( PARLISTCALL )",	None,	"TERM' NUMEXPR' EXPR'",	"TERM' NUMEXPR' EXPR'",	None,	"TERM' NUMEXPR' EXPR'",	"TERM' NUMEXPR' EXPR'",	"TERM' NUMEXPR' EXPR'",	None,	"TERM' NUMEXPR' EXPR'",	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,],
[None,	None,	"",	None,	None,	None,	None,	None,	None,	None,	None,	"id PARLISTCALL'",	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,],
[None,	None,	"",	None,	None,	", PARLISTCALL",None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,],
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
