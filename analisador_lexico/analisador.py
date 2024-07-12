import re

# Define padrões de token
token_patterns = [
    (r'\bdef\b', 'DEF'),
    (r'\bint\b', 'INT'),
    (r'\bprint\b', 'PRINT'),
    (r'\breturn\b', 'RETURN'),
    (r'\bif\b', 'IF'),
    (r'\belse\b', 'ELSE'),
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'ID'),
    (r'\d+', 'NUM'),
    (r'==', 'EQ'),
    (r'=', 'ASSIGN'),
    (r'\+', 'PLUS'),
    (r'-', 'MINUS'),
    (r'\*', 'TIMES'),
    (r'/', 'DIVIDE'),
    (r'<', 'LT'),
    (r'>', 'GT'),
    (r',', 'COMMA'),
    (r';', 'SEMICOLON'),
    (r'\(', 'LPAREN'),
    (r'\)', 'RPAREN'),
    (r'\{', 'LBRACE'),
    (r'\}', 'RBRACE'),
    (r'\s+', None),  # Espaços em branco (ignorar)
]

# Função de tokenização
def tokenize(code):
    pos = 0
    tokens = []
    while pos < len(code):
        match = None
        for token_pattern in token_patterns:
            pattern, tag = token_pattern
            regex = re.compile(pattern)
            match = regex.match(code, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            raise SyntaxError(f"Illegal character: {code[pos]}")
        else:
            pos = match.end(0)
    return tokens

# Exemplo de código
code = """
def main() {
    int x;
    int y;
    x = 5;
    y = x + 10;
    print y;
    if (x < y) {
        print x;
    } else {
        print y;
    }
    return;
}
"""

# Tokenizando o código
tokens = tokenize(code)
for token in tokens:
    print(token)
