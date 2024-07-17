import sys
from analisador_lexico import lex_analyser
from analisador_sintatico import syn_analyser
from utils import list_lsi_files
sys.path.append("../..")

"""
Autores:
Allan Cesar Ferreira (16200891)
Gabriel Guglielmi Kirtschig (21200417)
Kamilly Victória Ruseler (21204042)
"""

# Leitura do arquivo de dados
def read_data():
    print("Lista de arquivos: ")
    lsi_files = list_lsi_files()
    for file in lsi_files:
        print(file)
    nome_arquivo = input(str('Digite o nome do arquivo de entrada, com a extensão: '))
    try:
        with open(nome_arquivo, mode="r", encoding="utf-8") as file:
            dados = file.read()
            return dados
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado. Tente novamente.")



# Leitura do código de um arquivo
data = read_data()

# Análise léxica do código lido
tokens = lex_analyser(data)
print(f"Lista de tokens gerada: {tokens}")

# Análise sintática da lista de tokens gerada
result = syn_analyser(tokens)
print(f"A lista de tokens {tokens} é válida de acordo com a gramática: {result}")