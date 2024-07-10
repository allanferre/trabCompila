import re
# Exemplos da biblioteca do regex pra usar 
# Este exemplo usa regex para encontrar ocorrências da palavra ‘Python’ em um texto
# import re
# text = "Python é poderoso. Python é fácil de aprender."
# pattern = r'\\bPython\\b'
# matches = re.findall(pattern, text)
# print("Ocorrências de 'Python':", len(matches))

# Este exemplo usa a expressão regular \\s para 
# dividir a string em substrings sempre que encontra um espaço
# import re
# text = "Python é poderoso. Python é fácil de aprender."
# splitted_text = re.split('\\s', text)
# print(splitted_text)



def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
    lista_de_caracteres = re.split('\\s', conteudo)
    return lista_de_caracteres

def classificar_caracteres(lista_de_caracteres):
    tokens = []
    for caractere in lista_de_caracteres:
        if caractere.isdigit():
            tokens.append(('integer', int(caractere)))
        else:
            tokens.append(('string', caractere))
    return tokens

# Exemplo de uso:
lista_de_caracteres = ler_arquivo('arquivoLex.txt')
tokens = classificar_caracteres(lista_de_caracteres)
for token in tokens:
    print(token)






