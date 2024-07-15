# Tabela LL(1) revisada representada como um dicionário
parse_table = {
    'MAIN': {'def': ['FLIST'], 'int': ['STMT'], 'id': ['STMT'], 'print': ['STMT'], 'return': ['STMT'], 'if': ['STMT'], '{': ['STMT'], ';': ['STMT'], '$': []},
    'FLIST': {'def': ['FDEF', 'FLIST'], '$': []},
    'FDEF': {'def': ['def', 'id', '(', 'PARLIST', ')', '{', 'STMTLIST', '}']},
    'PARLIST': {'int': ['int', 'id', ',', 'PARLIST'], ')': [], '$': []},
    'STMT': {'int': ['int', 'id', ';'], 'id': ['ATRIBST', ';'], 'print': ['PRINTST', ';'], 'return': ['RETURNST', ';'], 'if': ['IFSTMT'], '{': ['{', 'STMTLIST', '}'], ';': [';']},
    'ATRIBST': {'id': ['id', '=', 'EXPR']},
    'FCALL': {'id': ['id', '(', 'PARLISTCALL', ')']},
    'PARLISTCALL': {'id': ['id', ',', 'PARLISTCALL'], ')': [], '$': []},
    'PRINTST': {'print': ['print', 'EXPR']},
    'RETURNST': {'return': ['return']},
    'IFSTMT': {'if': ['if', '(', 'EXPR', ')', 'STMT', 'else', 'STMT'], 'else': ['if', '(', 'EXPR', ')', 'STMT']},
    'STMTLIST': {'int': ['STMT', 'STMTLIST'], 'id': ['STMT', 'STMTLIST'], 'print': ['STMT', 'STMTLIST'], 'return': ['STMT', 'STMTLIST'], 'if': ['STMT', 'STMTLIST'], '{': ['STMT', 'STMTLIST'], ';': ['STMT', 'STMTLIST'], '}': [], '$': []},
    'EXPR': {'id': ['NUMEXPR'], 'num': ['NUMEXPR'], '(': ['NUMEXPR']},
    'NUMEXPR': {'id': ['TERM'], 'num': ['TERM'], '(': ['TERM']},
    'TERM': {'id': ['FACTOR'], 'num': ['FACTOR'], '(': ['FACTOR']},
    'FACTOR': {'id': ['id'], 'num': ['num'], '(': ['(', 'NUMEXPR', ')']}
}

def parse(tokens):
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

# Exemplos de tokens
examplos = [
    ["$","def", "(", "int", "id", ")", "{", "int", "id", "=", "num", ";", "}", ""],   
    ["$","def", "(", "int", "id", ")", "{", "", "}", ""],  
    ["$","int", "id", "=", "num", ";", ""],                                       
    ["$","print", "id", ";"],                                                  
    ["$","def", "(", "int", ")", "{", "int", "id", "=", "num", ";", "}", ""],     
    ["$","int", "id", "num", ";", ""],                                             
    ["$","num"],                                             
    ["$","return", "id", ";", ""],                                                 
    ["$","def", "(", "int", "id", ")", "{", "id", "=", "num", ";", "}"],
    ["$","def", "id", "(", "int", "id", ")", "{", "int", "id", ";", "}"],
    ["$","id", "=", "num", ";"],
    ["$","print", "num", ";"],
]

for tokens in examplos:
    result = parse(tokens)
    print(f"A lista de tokens {tokens} é válida de acordo com a gramática: {result}")
