# Este é um analisador descendente recursivo simples
def parse(tokens, grammar):
    # Inicialize o índice do token
    token_index = 0

    # Defina uma função para analisar um símbolo não terminal
    def parse_symbol(symbol, depth=0):
        nonlocal token_index
        
        # Verifique a profundidade
        if depth > 2:
            print("Erro: Profundidade máxima de recursão excedida")
            return False

        # Salve o índice do token atual
        saved_token_index = token_index

        # Se o símbolo é um símbolo terminal
        if symbol not in grammar:
            # Se o token atual corresponder ao símbolo, consuma o token e retorne True
            if token_index < len(tokens) and tokens[token_index] == symbol:
                token_index += 1
                return True
            else:
                if token_index < len(tokens):
                    print(f"Erro: esperava '{symbol}', obteve '{tokens[token_index]}'")
                else:
                    print(f"Erro: esperava '{symbol}', mas não há mais tokens")
                return False

        # Se o símbolo é um símbolo não terminal
        else:
            # Salve o índice do token atual
            saved_token_index = token_index
            # Tente cada produção alternativa
            for production in grammar[symbol]:
                # Redefina o índice do token
                token_index = saved_token_index

                # Tente analisar cada símbolo na produção
                if all(parse_symbol(s, depth+1) for s in production):
                    return True

            # Se nenhuma produção teve sucesso, retorne False
        return False

    # Comece a análise a partir do símbolo inicial
    return parse_symbol('MAIN') and token_index == len(tokens)

# Defina a gramática
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

# Defina a lista de tokens
tokens1 = ["def", "id", "(", "int", "id", ")", "{", "int", "id", ";", "}"]
tokens2 = ["def", "("]

# Verifique se a lista de tokens pertence à gramática
if parse(tokens1, grammar):
    print("YES! A lista de tokens pertence à gramática.")   
else:
    print("OPS! A lista de tokens não pertence à gramática.")
