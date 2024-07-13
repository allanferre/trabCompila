# INE5622 - INTRODUÇÃO A COMPILADORES

## Projeto em Equipe

> Allan Cesar Ferreira (16200891) - ferreiraallan19@gmail.com

> Gabriel Guglielmi Kirtschig (21200417) - gabrielguglielmik@gmail.com

> Kamilly Victória Ruseler (21204042) - kamiruseler@gmail.com

### Instruções

1. Para rodar o código em um ambiente virtual Python: `make run` ou então `python main.py`

3. O programa irá pedir para inserir qual arquivo você deseja executar. Insira o nome do arquivo junto com a extensão, exemplo: `sucesso_lexico.txt`

4. O resultado da análise aparecerá em seguida

### Estrutura do projeto

- **analisador_lexico.py**: 
contém toda a lógica do analisador léxico, incluindo os tokens (terminais e não terminais), o regex para verificar se o token está dentro da linguagem e a lógica que captura o erro e mostra em qual linha e coluna do arquivo txt ele ocorreu

- **arquivos de erro do analisador léxico**:
três arquivos .txt com mais de 15 linhas, que contém tokens não reconhecidos pela linguagem: !, % e ~
    - lexico_erro_!.txt
    - lexico_erro_%.txt
    - lexico_erro_~.txt

- **arquivo de sucesso**:
um arquivo com mais de 50 linhas, com um exemplo de sucesso para a nossa linguagem; demonstra o uso básico de funções, declaração e atribuição de variáveis
    - sucesso_lexico.txt

- **Makefile**:
um arquivo que contém uma sequência de instruções ao programa. usando o comando `make run`, é possível executar a main

- **utils.py**:
um arquivo destinado a funções complementares, como a lógica de percorrer uma lista dos arquivos .txt. 

- **main.py**:
fluxo principal do projeto, onde as demais funções são invocadas

- **.gitignore**:
utilizado para evitar o merge de arquivos não essenciais, como os de cache das execuções python