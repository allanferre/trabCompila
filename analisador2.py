import tabelaPreditiva as tabela
class Parser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.tokens = []
        self.current_token = None

    def parse(self, tokens):
        self.tokens = tokens
        self.current_token = self.tokens.pop(0)
        return self.statement('MAIN')

    def statement(self, stmt):
        if stmt not in self.grammar:
            return False

        for production in self.grammar[stmt]:
            if self.match(production):
                return True

        return False

    def match(self, production):
        tokens_backup = self.tokens[:]
        current_token_backup = self.current_token

        for symbol in production:
            if symbol in self.grammar:  # non-terminal
                if not self.statement(symbol):
                    self.tokens = tokens_backup[:]
                    self.current_token = current_token_backup
                    return False
            else:  # terminal
                if self.current_token == symbol:
                    if self.tokens:
                        self.current_token = self.tokens.pop(0)
                else:
                    self.tokens = tokens_backup[:]
                    self.current_token = current_token_backup
                    return False

        return True


# Define the grammar
grammar = tabela
grammar1 = {
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

# Create a parser
parser = Parser(grammar)

# Define the tokens
tokens1 = ["def", "id", "(", "int", "id", ")", "{", "int", "id", ";", "}"]
tokens2 = ["def", "("]

# Parse the tokens
result1 = parser.parse(tokens1)
result2 = parser.parse(tokens2)

# Print the results
print(f"tokens1 pertence à gramática: {result1}")
print(f"tokens2 pertence à gramática: {result2}")

