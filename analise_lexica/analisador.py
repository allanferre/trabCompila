import os

class Lexico:
    """
    Analisador léxico baseado na máquina de Turing (autômatos)

    - fita: dividida em células, uma adjacente à outra. Cada célula 
    contém um símbolo de algum alfabeto finito

    - cabeca: pode ler e escrever símbolos na fita e mover-se para a 
    esquerda ou para a direita

    - tabela_de_simbolos: função de transição que diz à máquina que 
    símbolo escrever, como mover o cabeçote (para esquerda e para direita)
    e qual será seu novo estado, dados o símbolo que ele acabou de ler na fita
    e o estado em que se encontra. Se não houver entrada alguma na tabela para 
    a combinação atual de símbolo e estado então a máquina para.
    """
    def __init__(self, arquivo_fonte):
        self.__cabeca = 0
        self.__fita = []
        self.__numero_linha = 0
        self.__tabela_de_simbolos = []
        self.__lexema = ""
        self.__fim_linha = '\n'
        self.__arquivo_fonte = open(arquivo_fonte, 'r') if os.path.exists(arquivo_fonte) else None
        if not self.__arquivo_fonte:
            print("Erro: arquivo fonte não encontrado")
            exit()
        
    def __avancar_cabeca(self):
        self.__cabeca += 1
    
    def __posicao_cabeca(self):
        return self.__cabeca
    
    def __atualizar_numero_linha(self):
        self.__numero_linha += 1

    def __obter_caracter(self):
        if self.__cabeca < len(self.__fita):
            letra = self.__fita[self.__cabeca]
            self.__avancar_cabeca()
            if letra != self.__fim_linha:
                self.__lexema += letra
            return letra
        return None

    def obter_tabela_simbolos(self):
        """
        Chama o método q0 do estado inicial, que decide qual o próximo
        estado do autômato (por exemplo: lê "0" e vai do q0 para o q1)
        """
        for linha in self.__arquivo_fonte:
            self.__fita = list(linha)
            self.__q0()
            self.__atualizar_numero_linha()
            self.__cabeca = 0
        self.__arquivo_fonte.close()
        return self.__tabela_de_simbolos
    
    def __q0(self):
        self.__caracter = self.__obter_caracter()
        if self.__caracter is None:
            return
        elif self.__caracter.isspace():
            self.__lexema = ''
            self.__q0()
        elif self.__caracter.isalpha():
            self.__q_identifier_or_keyword()
        elif self.__caracter.isdigit():
            self.__q_number()
        elif self.__caracter in ['(', ')', '{', '}', ',', ';', '+', '-', '*', '=', '<', '>', '!']:
            self.__q_symbol()
        else: 
            self.__erro_lexico()

    def __q_identifier_or_keyword(self):
        self.__caracter = self.__obter_caracter()
        while self.__caracter and (self.__caracter.isalnum() or self.__caracter == '_'):
            self.__caracter = self.__obter_caracter()

        if self.__caracter:
            self.__cabeca -= 1
            self.__lexema = self.__lexema[:-1]

        if self.__lexema in ["def", "int", "return", "print", "if", "else"]:
            self.__tabela_de_simbolos.append([self.__lexema.upper(), self.__lexema, self.__numero_linha, self.__cabeca])
        else:
            self.__tabela_de_simbolos.append(["ID", self.__lexema, self.__numero_linha, self.__cabeca])
        self.__lexema = ''
        self.__q0()

    def __q_number(self):
        self.__caracter = self.__obter_caracter()
        while self.__caracter and self.__caracter.isdigit():
            self.__caracter = self.__obter_caracter()

        if self.__caracter:
            self.__cabeca -= 1
            self.__lexema = self.__lexema[:-1]

        self.__tabela_de_simbolos.append(["NUM", self.__lexema, self.__numero_linha, self.__cabeca])
        self.__lexema = ''
        self.__q0()

    def __q_symbol(self):
        if self.__caracter in ['+', '-', '*', '=', '<', '>']:
            next_char = self.__obter_caracter()
            if next_char and next_char == '=':
                self.__lexema += '='
            else:
                self.__cabeca -= 1
                self.__lexema = self.__lexema[:-1]

        self.__tabela_de_simbolos.append([self.__caracter, self.__caracter, self.__numero_linha, self.__cabeca])
        self.__lexema = ''
        self.__q0()

    def __erro_lexico(self):
        print ("Erro léxico: ({0}, {1}): caracter {2} inesperado".format(self.__numero_linha, self.__cabeca, self.__caracter))
        exit()

def main():
    arquivo = "analise_lexica/fonte_erros.txt"
    automato = Lexico(arquivo_fonte=arquivo)
    tabela_simbolos = automato.obter_tabela_simbolos()
    for simbolo in tabela_simbolos:
        print(simbolo)

if __name__ == '__main__':
    main()
