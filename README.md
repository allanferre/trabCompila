# INE5622 - INTRODUÇÃO A COMPILADORES

## Projeto em Equipe

> Allan Cesar Ferreira (16200891) - ferreiraallan19@gmail.com

> Gabriel Guglielmi Kirtschig (21200417) - gabrielguglielmik@gmail.com

> Kamilly Victória Ruseler (21204042) - kamiruseler@gmail.com

### Instruções

1. Para rodar o código em um ambiente virtual Python: `make run` ou então `python main.py`

3. O programa irá pedir para inserir qual arquivo você deseja executar. Insira o nome do arquivo junto com a extensão, exemplo: `sucesso.lsi`

4. O resultado da análise aparecerá em seguida

### Estrutura do projeto

- **analisador_lexico.py**: 
contém toda a lógica do analisador léxico, incluindo os tokens (terminais e não terminais), o regex para verificar se o token está dentro da linguagem e a lógica que captura o erro e mostra em qual linha e coluna do arquivo lsi ele ocorreu


- **Arquivos de erro do analisador léxico**:
três arquivos .lsi com mais de 15 linhas, que contém tokens não reconhecidos pela linguagem: !, % e ~
    - lexico_erro_!.lsi
    - lexico_erro_%.lsi
    - lexico_erro_~.lsi
      

- **Arquivo de sucesso**:
um arquivo com mais de 50 linhas, com um exemplo de sucesso para a nossa linguagem; demonstra o uso básico de funções, declaração e atribuição de variáveis
    - sucesso.lsi
      

- **Makefile**:
um arquivo que contém uma sequência de instruções ao programa. usando o comando `make run`, é possível executar a main


- **utils.py**:
um arquivo destinado a funções complementares, como a lógica de percorrer uma lista dos arquivos .lsi.


- **main.py**:
fluxo principal do projeto, onde as demais funções são invocadas


- **.gitignore**:
utilizado para evitar o merge de arquivos não essenciais, como os de cache das execuções python


- **analisador_sintatico.py**: 
contém toda a lógica do analisador léxico, incluindo a gramática no começo do código seguido da função que executa a análise sintática. A função da análise sintática inicia pela primeira gramática MAIN e cria a pilha de tokens vazia, em segue coleta o primeiro token da pilha e o compara com a primeira regra da gramática e caso haja mais tokens para ser analisado a função continua executando até o fim da pilha.


- **Arquivos de erro do analisador sintatico**:
três arquivos .lsi com mais de 15 linhas, que contém tokens não reconhecidos pela gramatica
    - sintatico_erro_;.lsi
    - sintatico_erro_).lsi
    - sintatico_erro_}.lsi
      

- **Arquivo de sucesso do analisador sintatico**:
um arquivo com mais de 50 linhas, com um exemplo de sucesso para a nossa linguagem; demonstra o uso básico de funções, declaração e atribuição de variáveis
    - sucesso.lsi
      

- **Arquivo com a definição dos analisadores**:
um arquivo com mais definições/detalhes sobre lógica dos analisadores.
    - definicoes_analisadores.txt


- **Arquivos para inserção de input**:
  dois arquivos para editar os inputs e realizar testes.
    - sintatico_teste.lsi
    - lexico_teste.lsi


- **Executando o projeto em ambiente Linuxt**:
  dois arquivos para editar os inputs e realizar testes.
    - abra o terminal
    - navegue até o diretório onde o projeto se encontra
    - se o ambiente não estiver com o python instalado vc pode rodar o comando 'sudo apt-get install python3'
    - por fim, para executar o projeto basta rodar o arquivo main.py com o comando 'python main.py'
