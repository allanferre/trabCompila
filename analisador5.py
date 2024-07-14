class SyntaxRecognizer:
    def __init__(self, table):
        self.table = table
        self.non_terminals = ["FLIST", "FLIST'", "FDEF", "PARLIST", "PARLIST'", "STMT", "STMT'", "STMLIST", "STMLIST'", "ATRIBST", "ATRIBST'", "IFSTMT", "IFSTMT'", "PRINTST", "RETURNST", "EXPR", "EXPR'", "NUMEXPR", "NUMEXPR'", "TERM", "TERM'", "FACTOR", "PARLISTCALL", "PARLISTCALL'"]
        self.terminals = ["def", "(", ")", "{", "}", "int", "id", ";", "=", "if", "else", "print", "return", "==", "<", ">", "+", "-", "*", "num", ""]

    def parse(self, tokens):
        stack = ["FLIST"]
        tokens.append("")
        index = 0

        while len(stack) > 0:
            top = stack.pop()
            if top in self.terminals:
                if top == tokens[index]:
                    index += 1
                else:
                    return False
            elif top in self.non_terminals:
                rule = self.table[self.non_terminals.index(top)][self.terminals.index(tokens[index])]
                if rule:
                    stack.extend(reversed(rule.split()))
                else:
                    return False
            else:
                return False

        return index == len(tokens) - 1

table = [		
    [None, None, None, None, None, None, None, "STMT", None, None, None, "STMT", "FLIST", "STMT", None, None, "STMT", "STMT", "STMT", "STMT", None, ""],
    [None, None, None, None, None, None, None, None, None, None, None, None, "FDEF FLIST'", None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, "FDEF", None, None, None, None, None, None, None, None, ""],
    [None, None, None, None, None, None, None, None, None, None, None, None, "def ( PARLIST ) { STMLIST }", None, None, None, None, None, None, None, None],
    [None, None, "", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, "int id PARLIST'", None, None],
    [None, None, "", None, None, ", PARLIST", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, ";", None, None, None, "ATRIBST ;", None, "IFSTMT", None, None, "PRINTST ;", "RETURNST ;", "int id", "{ STMLIST' }", None, None],
    [None, None, None, None, None, None, None, None, None, None, None, "id = ATRIBST'", None, None, None, None, None, None, None, None, None],
    [None, "FACTOR TERM' NUMEXPR' EXPR'", None, None, None, None, None, None, None, None, None, "id TEST", None, None, None, "FACTOR TERM' NUMEXPR' EXPR'", None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, "print EXPR", None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, "return", None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, "if ( EXPR ) STMT IFSTMT'", None, None, None, None, None, None],
    [None, None, None, None, None, None, None, "", None, None, None, "", None, "", ["", "else"], None, "", "", "", "", "", ""],
    [None, None, None, None, None, None, None, "STMT STMLIST'", None, None, None, "STMT STMLIST'", None, "STMT STMLIST'", None, None, "STMT STMLIST'", "STMT STMLIST'", "STMT STMLIST'", "STMT STMLIST'", None],
    [None, "NUMEXPR EXPR'", None, None, None, None, None, None, None, None, None, None, None, None, None, "NUMEXPR EXPR'", None, None, None, None, None],
    ["== NUMEXPR", None, "", None, None, None, None, "", "< NUMEXPR", None, "> NUMEXPR", None, None, None, None, None, None, None, None, None, None],
    [None, "TERM NUMEXPR'", None, None, None, None, None, None, None, None, None, None, None, None, None, "TERM NUMEXPR'", None, None, None, None],
    ["", None, "", None, "+ TERM NUMEXPR'", None, "- TERM NUMEXPR'", "", "", None, "", None, None, None, None, None, None, None, None, None],
    [None, "FACTOR TERM'", None, None, None, None, None, None, None, None, None, None, None, None, None, "FACTOR TERM'", None, None, None, None],
    ["", None, "", "* FACTOR TERM'", "", None, "", "", "", None, "", None, None, None, None, None, None, None, None, None],
    [None, "( NUMEXPR )", None, None, None, None, None, None, None, None, None, None, None, None, None, "num", None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, "id ( PARLISTCALL )", None, None, None, None, None, None, None, None],
    ["TERM' NUMEXPR' EXPR'", "( PARLISTCALL )", None, "TERM' NUMEXPR' EXPR'", "TERM' NUMEXPR' EXPR'", None, "TERM' NUMEXPR' EXPR'", "TERM' NUMEXPR' EXPR'", "TERM' NUMEXPR' EXPR'", None, "TERM' NUMEXPR' EXPR'", None, None, None, None, None],
    [None, None, "", None, None, None, None, None, None, None, None, "id PARLISTCALL'", None, None, None, None, None, None, None, None],
    [None, None, "", None, None, ", PARLISTCALL", None, None, None, None, None, None, None, None, None, None, None, None, None, None]
]

recognizer = SyntaxRecognizer(table)

# Exemplos de tokens
examples = [
    ["def", "(", "int", "id", ")", "{", "id", "=", "num", ";", "}"], # Pertence
    # ["print", "id", ";"],                                           # Pertence
    # ["if", "(", "id", "==", "num", ")", "id", "=", "num", ";"],     # Pertence
    # ["def", "(", "int", ")", "{", "id", "=", "num", ";", "}"],      # Não pertence
    # ["int", "id", "num", ";"],                                      # Não pertence
    # ["num"],                                          # Não pertence
]

for tokens in examples:
    result = recognizer.parse(tokens)
    print(f"Tokens: {tokens} -> {'Pertence' if result else 'Não Pertence'}")
