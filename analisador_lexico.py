import re

"""
Autores:
Allan Cesar Ferreira (16200891)
Gabriel Guglielmi Kirtschig (21200417)
Kamilly Victória Ruseler (21204042)

"""


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
    line = 1
    col = 1
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
                    token = (text, tag, line, col)
                    tokens.append(token)
                break
        if not match:
            raise SyntaxError(f"Caractere não reconhecido na linha {line}, coluna {col}: {code[pos]}")
        else:
            newlines = text.count('\n')
            if newlines > 0:
                line += newlines
                col = len(text) - text.rfind('\n')
            else:
                col += len(text)
            pos = match.end(0)
    
    return tokens
