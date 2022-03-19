# Aula 08: Lidando com módulos
# Importação de classes, métodos e construção de funções anônimas(lambda)

# ================= Exemplo 8.3 =================
# Funções anônimas

contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['Cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b

print(soma(5, 10))
print(subtracao(10, 5))

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
}

print(type(calculadora))
soma = calculadora['soma']
multiplicadao = calculadora['multiplicacao']
print('A soma é: {}'.format(soma(10, 5)))
print('A multiplicação é: {}'.format(multiplicadao(10, 2)))
