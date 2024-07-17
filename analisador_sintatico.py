"""
Autores:
Allan Cesar Ferreira (16200891)
Gabriel Guglielmi Kirtschig (21200417)
Kamilly Victória Ruseler (21204042)
"""

# Tabela LL(1) revisada representada como um dicionário
parse_table = {
    'MAIN': {'def': ['FLIST'], 'int': ['STMT'], 'id': ['STMT'], 'print': ['STMT'], 'return': ['STMT'], 'if': ['STMT'], '{': ['STMT'], ';': ['STMT'], '$': []},
    'FLIST': {'def': ['FDEF', 'FLIST'], '$': []},
    'FDEF': {'def': ['def', 'id', '(', 'PARLIST', ')', '{', 'STMTLIST', '}']},
    'PARLIST': {'int': ['int', 'id', 'PARLISTTAIL'], ')': [], '$': []},
    'PARLISTTAIL': {',': [',', 'int', 'id', 'PARLISTTAIL'], ')': []},
    'STMT': {'int': ['int', 'id', ';'], 'id': ['ATRIBST'], 'print': ['PRINTST', ';'], 'return': ['RETURNST', ';'], 'if': ['IFSTMT'], '{': ['{', 'STMTLIST', '}'], ';': [';']},
    'ATRIBST': {'id': ['id', '=', 'EXPR', ';']},
    'FCALL': {'id': ['id', '(', 'PARLISTCALL', ')']},
    'PARLISTCALL': {'id': ['id', 'PARLISTCALLTAIL'], ')': [], '$': []},
    'PARLISTCALLTAIL': {',': [',', 'id', 'PARLISTCALLTAIL'], ')': []},
    'PRINTST': {'print': ['print', 'EXPR']},
    'RETURNST': {'return': ['return', 'EXPR'], ';': ['return', ';']},
    'IFSTMT': {'if': ['if', '(', 'EXPR', ')', 'STMT', 'ELSEPART']},
    'ELSEPART': {'else': ['else', 'STMT'], '': [], '$': []},
    'STMTLIST': {'int': ['STMT', 'STMTLIST'], 'id': ['STMT', 'STMTLIST'], 'print': ['STMT', 'STMTLIST'], 'return': ['STMT', 'STMTLIST'], 'if': ['STMT', 'STMTLIST'], '{': ['STMT', 'STMTLIST'], ';': ['STMT', 'STMTLIST'], '}': [], '$': []},
    'EXPR': {'id': ['NUMEXPR', 'EXPRTAIL'], 'num': ['NUMEXPR', 'EXPRTAIL'], '(': ['NUMEXPR', 'EXPRTAIL'], ';': [';', '}']},
    'EXPRTAIL': {'+': ['+', 'NUMEXPR', 'EXPRTAIL'], '-': ['-', 'NUMEXPR', 'EXPRTAIL'], '==': ['==', 'NUMEXPR', 'EXPRTAIL'], '$': [], ')': [], ';': []},
    'NUMEXPR': {'id': ['TERM', 'NUMEXPRTAIL'], 'num': ['TERM', 'NUMEXPRTAIL'], '(': ['TERM', 'NUMEXPRTAIL']},
    'NUMEXPRTAIL': {'+': ['+', 'TERM', 'NUMEXPRTAIL'], '-': ['-', 'TERM', 'NUMEXPRTAIL'], '$': [], ')': [], ';': [], '==': ['==', 'TERM', 'NUMEXPRTAIL']},
    'TERM': {'id': ['FACTOR', 'TERMTAIL'], 'num': ['FACTOR', 'TERMTAIL'], '(': ['FACTOR', 'TERMTAIL']},
    'TERMTAIL': {'*': ['*', 'FACTOR', 'TERMTAIL'], '$': [], ')': [], ';': [], '+': [], '-': [], '==': []},
    'FACTOR': {'id': ['id'], 'num': ['num'], '(': ['(', 'EXPR', ')']}
}

# Função de análise sintática
def syn_analyser(tokens):
    stack = ['MAIN', '$']
    tokens.append('$')
    index = 0
    
    while stack:
        top = stack.pop()
        current_token = tokens[index]
        
        if top in parse_table:
            if current_token in parse_table[top]:
                production = parse_table[top][current_token]
                if production:
                    stack.extend(reversed(production))
            else:
                print(f"Error: unexpected token {current_token} at position {index}")
                return False
        else:
            if top == current_token:
                index += 1
            else:
                print(f"Error: expected {top}, but found {current_token} at position {index}")
                return False
    
    if index == len(tokens) - 1:
        return True
    else:
        print("Error: tokens left in the input")
        return False