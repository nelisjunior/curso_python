# Aula 08: Lidando com módulos
# Importação de classes, métodos e construção de funções anônimas(lambda)

# ================= Exemplo 8.1 =================

from aula07_televisao import Televisao
from aula07_calculadora1 import Calculadora
from aula08_contador_letras import contador_letras, teste

televisao = Televisao()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)
calculadora = Calculadora(5, 10)
print(calculadora.soma())
lista = ['cachorro', 'gato', 'elefante']
total_letras = contador_letras(lista)
print('total de letras por palavra de lista: {}'.format(total_letras))
print(teste())
