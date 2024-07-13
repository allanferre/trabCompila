# Define the grammar
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

# Initialize the parsing table
parsing_table = {}

# Iterate over each non-terminal in the grammar
for non_terminal in grammar:
    # Initialize the row for the non-terminal
    parsing_table[non_terminal] = {}
    
    # Iterate over each production for the non-terminal
    for production in grammar[non_terminal]:
        # If the production is not empty
        if production:
            # The first symbol in the production is the input symbol for the parsing table
            input_symbol = production[0]
            
            # If the input symbol is not already in the row, add it
            if input_symbol not in parsing_table[non_terminal]:
                parsing_table[non_terminal][input_symbol] = []
            
            # Add the production to the cell in the parsing table for the non-terminal and input symbol
            parsing_table[non_terminal][input_symbol].append(production)

# Print the parsing table
for non_terminal in parsing_table:
    print(non_terminal + ":")
    for input_symbol in parsing_table[non_terminal]:
        print("  " + input_symbol + ": " + str(parsing_table[non_terminal][input_symbol]))
    print()

# Save the parsing table to a file
with open("parsing_table.txt", "w") as file:
    for non_terminal in parsing_table:
        file.write(non_terminal + ":\n")
        for input_symbol in parsing_table[non_terminal]:
            file.write("  " + input_symbol + ": " + str(parsing_table[non_terminal][input_symbol]) + "\n")
        file.write("\n")

print("The parsing table was successfully saved to parsing_table.txt")

