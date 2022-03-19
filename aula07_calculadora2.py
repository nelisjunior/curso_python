# Aula 7: construindo métodos, funções e classes em Python

# ================= Exemplo 7.2 =================
# Definições e classes

class Calculadora:

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

print(__name__)
if __name__ == '__main__':

    calculadora = Calculadora()
    print(calculadora.soma(10, 2))
    print(calculadora.subtracao(5, 3))
    print(calculadora.multiplicacao(100, 2))
    print(calculadora.divisao(10, 5))
