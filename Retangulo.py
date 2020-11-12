# Autor: Henrique Rosa Carvalho
# Aula 07 - Orientação a Objetos
'''
▷Construa um algoritmo para implementar a classe Retângulo que possui os atributos: altura e largura.
▷A classe deve ter os seguintes métodos:
	○Método construtor
	○Método que calcula a área do retângulo ( altura * largura) e retorna o resultado
	○Método que imprime os valores dos atributos da classe.

'''

class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcularArea(self):
        area = int(self.altura) * int(self.largura)
        return area

    def imprimirAltLarg(self):
        print("Altura = ", self.altura)
        print("Largura = ", self.largura)

resultado = Retangulo(8, 6)
Retangulo.imprimirAltLarg(resultado)
print("Área = ", Retangulo.calcularArea(resultado))