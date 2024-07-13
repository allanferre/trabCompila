def generate_parsing_table_from_grammar(grammar):
    parsing_table = {}

    for non_terminal, productions in grammar.items():
        parsing_table[non_terminal] = {}
        for production in productions:
            if not production:
                parsing_table[non_terminal][''] = [production]
            else:
                first_symbol = production[0]
                if first_symbol not in parsing_table[non_terminal]:
                    parsing_table[non_terminal][first_symbol] = []
                parsing_table[non_terminal][first_symbol].append(production)

    return parsing_table

def write_parsing_table_to_file(parsing_table, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for non_terminal, rules in parsing_table.items():
            file.write(f"{non_terminal}:\n")
            for terminal, productions in rules.items():
                formatted_productions = [" ".join(prod) for prod in productions]
                file.write(f"  {terminal}: {formatted_productions}\n")

# Defina a gramática conforme o código fornecido
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

# Gere a tabela de análise sintática
parsing_table = generate_parsing_table_from_grammar(grammar)

# Escreva a tabela em um arquivo de saída
write_parsing_table_to_file(parsing_table, 'parsing_table_generated.txt')
