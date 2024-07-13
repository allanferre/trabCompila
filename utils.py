import os

"""
Autores:
Allan Cesar Ferreira (16200891)
Gabriel Guglielmi Kirtschig (21200417)
Kamilly Victória Ruseler (21204042)
"""

def list_lsi_files():
    """
    Função complementar que lista todos os arquivos que terminam com .txt
    e os ordenam de forma alfabética, para mostrar ao usuário as opções
    possíveis de teste.
    """
    files = [f for f in os.listdir('.') if f.endswith('.lsi')]
    files.sort()
    return files