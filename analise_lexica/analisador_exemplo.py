import os

"""

EXEMPLO 
Vídeo 1: https://www.youtube.com/watch?v=pud18CZ81VE&ab_channel=EdWilsonTavaresFerreira
Vídeo 2: https://www.youtube.com/watch?v=TnCCGaY14Xo&ab_channel=EdWilsonTavaresFerreira

"""


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
        self.cabeca = 0
        self.fita = []
        self.numero_linha = 0
        self.tabela_de_simbolos = []
        self.lexema = ""
        self.fim_linha = '\n'
        self.arquivo_fonte = arquivo_fonte

        if os.path.exists(arquivo_fonte):
            """
            Se houver um arquivo, ele será aberto no modo R = read
            """
            self.arquivo_fonte = open(arquivo_fonte, 'r')
        else: 
            print("Erro: arquivo fonte não encontrado")
        
    def avancar_cabeca(self):
        self.cabeca += 1
    
    def posicao_cabeca(self):
        return self.cabeca
    
    def atualizar_numero_linha(self):
        self.numero_linha += 1

    def obter_caracter(self):
        if self.cabeca < len(self.fita):
            letra = self.fita[self.cabeca]
            self.avancar_cabeca()
            if letra != self.fim_linha and not letra.isspace():
                self.lexema += letra
            return letra
        return None
    
    def obter_tabela_simbolos(self):
        """
        Chama o método q0 do estado inicial, que decide qual o próximo
        estado do autômato (por exemplo: lê "0" e vai do q0 para o q1)
        """
        for linha in self.arquivo_fonte:
            self.fita = list(linha)
            self.q0()
            self.atualizar_numero_linha()
            self.cabeca = 0
        self.arquivo_fonte.close()
        return self.tabela_de_simbolos
    
    def q0(self):
        self.caracter = self.obter_caracter()
        if 'e' == self.caracter:
            self.q1() # estado q1
        elif 'l' == self.caracter:
            self.q8()
        elif self.caracter and (self.caracter.isdigit() or self.caracter.islower()):
            self.q12() # se for um dígito ou uma letra
        elif self.fim_linha == self.caracter:
            pass # finaliza a função 
        elif self.caracter and self.caracter.isspace():
            self.lexema = ''
            self.q0() # se for espaço, inicializa lexema e volta para estado q0
        else: 
            print ("Erro léxico: ({0}, {1}): caracter {2} inesperado".format(self.numero_linha, self.cabeca, self.caracter))
            exit()
        
    def q1(self):
        self.caracter = self.obter_caracter()
        if 's' == self.caracter:
            self.q2()
        elif self.fim_linha == self.caracter:
            pass
        elif self.caracter and self.caracter.isspace():
            self.lexema = ''
            self.q0()
        elif self.caracter and (self.caracter.isdigit() or self.caracter.islower()):
            self.q12()
        else:
            print ("Erro léxico: ({0}, {1}): caracter {2} inesperado".format(self.numero_linha, self.cabeca, self.caracter))
            exit()
    
    def q2(self):
        self.caracter = self.obter_caracter()
        if 'c' == self.caracter:
            self.q3()
        elif self.fim_linha == self.caracter:
            pass
        elif self.caracter and self.caracter.isspace():
            self.lexema = ''
            self.q0()
        elif self.caracter and (self.caracter.isdigit() or self.caracter.islower()):
            self.q12()
        else:
            print ("Erro léxico: ({0}, {1}): caracter {2} inesperado".format(self.numero_linha, self.cabeca, self.caracter))
            exit()
    
    def q3(self):
        self.caracter = self.obter_caracter()
        if 'r' == self.caracter:
            self.q4()
        elif self.fim_linha == self.caracter:
            pass
        elif self.caracter and self.caracter.isspace():
            self.lexema = ''
            self.q0()
        elif self.caracter and (self.caracter.isdigit() or self.caracter.islower()):
            self.q12()
        else:
            print ("Erro léxico: ({0}, {1}): caracter {2} inesperado".format(self.numero_linha, self.cabeca, self.caracter))
            exit()

    def q4(self):
        self.caracter = self.obter_caracter()
        if 'e' == self.caracter:
            self.q5()
        elif self.fim_linha == self.caracter:
            pass
        elif self.caracter and self.caracter.isspace():
            self.lexema = ''
            self.q0()
        elif self.caracter and (self.caracter.isdigit() or self.caracter.islower()):
            self.q12()
        else:
            print ("Erro léxico: ({0}, {1}): caracter {2} inesperado".format(self.numero_linha, self.cabeca, self.caracter))
            exit()

    def q5(self):
        self.caracter = self.obter_caracter()
        if 'v' == self.caracter:
            self.q6()
        elif self.fim_linha == self.caracter:
            pass
        elif self.caracter and self.caracter.isspace():
            self.lexema = ''
            self.q0()
        elif self.caracter and (self.caracter.isdigit() or self.caracter.islower()):
            self.q12()
        else:
            print ("Erro léxico: ({0}, {1}): caracter {2} inesperado".format(self.numero_linha, self.cabeca, self.caracter))
            exit()

    def q6(self):
        self.caracter = self.obter_caracter()
        if 'a' == self.caracter:
            self.q7()
        elif self.fim_linha == self.caracter:
            pass
        elif self.caracter and self.caracter.isspace():
            self.lexema = ''
            self.q0()
        elif self.caracter and (self.caracter.isdigit() or self.caracter.islower()):
            self.q12()
        else:
            print ("Erro léxico: ({0}, {1}): caracter {2} inesperado".format(self.numero_linha, self.cabeca, self.caracter))
            exit()

    def q7(self):
        """Reconhece o comando 'escreva' """
        self.caracter = self.obter_caracter()
        if self.fim_linha == self.caracter:
            self.tabela_de_simbolos.append(["ESCREVA", self.lexema, self.numero_linha, self.cabeca])
            self.lexema = ''
        elif self.caracter and self.caracter.isspace(): #deve ser lido o próximo token sem quebrar linha
            self.lexema = self.lexema[:len(self.lexema)-1] #espaço é descartado
            self.tabela_de_simbolos.append(["ESCREVA", self.lexema, self.numero_linha, self.cabeca])
            self.lexema = ''
            self.q0()
        elif self.caracter and (self.caracter.isdigit() or self.caracter.islower()):
            self.q12() # significa que é um identificador e vai para q12
        else:
            print ("Erro léxico: ({0}, {1}): caracter {2} inesperado".format(self.numero_linha, self.cabeca, self.caracter))

    def q8(self):
        self.caracter = self.obter_caracter()
        if 'e' == self.caracter:
            self.q9()
        elif self.fim_linha == self.caracter:
            pass
        elif self.caracter and self.caracter.isspace():
            self.lexema = ''
            self.q0()
        elif self.caracter and (self.caracter.isdigit() or self.caracter.islower()):
            self.q12()
        else:
            print ("Erro léxico: ({0}, {1}): caracter {2} inesperado".format(self.numero_linha, self.cabeca, self.caracter))
            exit()

    def q9(self):
        self.caracter = self.obter_caracter()
        if 'i' == self.caracter:
            self.q10()
        elif self.fim_linha == self.caracter:
            pass
        elif self.caracter and self.caracter.isspace():
            self.lexema = ''
            self.q0()
        elif self.caracter and (self.caracter.isdigit() or self.caracter.islower()):
            self.q12
        elif self.caracter and (self.caracter.isdigit() or self.caracter.islower()):
            self.q12()
        else:
            print("Erro léxico: ({0}, {1}): caracter {2} inesperado".format(self.numero_linha, self.cabeca, self.caracter))
            exit()

    def q10(self):
        self.caracter = self.obter_caracter()
        if 'a' == self.caracter:
            self.q11()
        elif self.fim_linha == self.caracter:
            pass
        elif self.caracter and self.caracter.isspace():
            self.lexema = ''
            self.q0()
        elif self.caracter and (self.caracter.isdigit() or self.caracter.islower()):
            self.q12()
        else:
            print("Erro léxico: ({0}, {1}): caracter {2} inesperado".format(self.numero_linha, self.cabeca, self.caracter))
            exit()

    def q11(self):
        """Reconhece o comando 'leia'"""
        self.caracter = self.obter_caracter()
        if self.fim_linha == self.caracter:
            self.tabela_de_simbolos.append(["LEIA", self.lexema, self.numero_linha, self.cabeca])
            self.lexema = ''
        elif self.caracter and self.caracter.isspace(): #deve ser lido o próximo token sem quebrar linha
            self.lexema = self.lexema[:len(self.lexema) - 1] #espaço é descartado
            self.tabela_de_simbolos.append(["LEIA", self.lexema, self.numero_linha, self.cabeca])
            self.lexema = ''
            self.q0()
        elif self.caracter and (self.caracter.isdigit() or self.caracter.islower()):
            self.q12() # significa que é um identificador e vai para q12
        else:
            print("Erro léxico: ({0}, {1}): caracter {2} inesperado".format(self.numero_linha, self.cabeca, self.caracter))
            exit()

    def q12(self):
        """Reconhece identificadores"""
        self.caracter = self.obter_caracter()
        while self.caracter and (self.caracter.isdigit() or self.caracter.islower()):
            self.caracter = self.obter_caracter()
        if self.fim_linha == self.caracter:
            self.tabela_de_simbolos.append(["ID", self.lexema, self.numero_linha, self.cabeca])
            self.lexema = ''
        elif self.caracter and self.caracter.isspace():
            self.lexema = self.lexema[:len(self.lexema) - 1] #espaço é descartado
            self.tabela_de_simbolos.append(["ID", self.lexema, self.numero_linha, self.cabeca])
            self.lexema = ''
            self.q0()
        else:
            print("Erro léxico: ({0}, {1}): caracter {2} inesperado".format(self.numero_linha, self.cabeca, self.caracter))
            exit()
        
def main():
    arquivo = "analise_lexica/fonte_exemplo.txt"
    automato = Lexico(arquivo_fonte=arquivo)
    tabela_simbolos = automato.obter_tabela_simbolos()
    for simbolo in tabela_simbolos:
        print(simbolo)

if __name__ == '__main__':
    main()
