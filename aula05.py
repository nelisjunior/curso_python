# Aula 5: criando nossa primeira lista!

# ============= ===== Exemplo 5.4 ==================
# Convertendo listas para tuplas!
lista = [12, 10, 3, 7, 5]
lista_animal = ['cachorro',
                'gato',
                'elefante',
                'lobo',
                'arara'
                ]

print('\nLista de animais [antes]:\n', lista_animal)
lista_animal[0] = 'macaco'
print('\nLista de animais [depois]:\n', lista_animal)

tupla = (1, 10, 12, 14)
print(len(tupla))
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)

# # ============= ===== Exemplo 5.3 ==================
# # Trabalhando com tuplas(listas imutáveis)!
# lista = [12, 10, 3, 7, 5]
# lista_animal = ['cachorro',
#                 'gato',
#                 'elefante',
#                 'lobo',
#                 'arara'
#                 ]
#
# print('\nLista de animais [antes]:\n', lista_animal)
# lista_animal[0] = 'macaco'
# print('\nLista de animais [depois]:\n', lista_animal)
#
# tupla = (1, 10, 12, 14)
# print('\nValores tupla: ', tupla,
#       '.\nTotal de objetos: ', len(lista_animal))

# # ============= ===== Exemplo 5.2 ==================
# # Ordenação de listas!
# lista = [12, 10, 3, 7, 5]
# lista_animal = ['cachorro', 'gato', 'elefante', 'logo', 'arara']
#
# lista.sort()
# lista_animal.sort()
#
# print(lista)
# print(lista_animal)
# lista_animal.reverse()
# print(lista_animal)

# ============= ===== Exemplo 5.1: ==================
# manipulando listas

# lista = {1, 3, 5, 7} # é possível haver vários tipos de valores numa mesma lista, porém, o ideal é diferenciar as listas para os diferentes tipos de valores.
# lista_animal = ['cachorro', 'gato', 'elefante']
# # print(lista_animal[1])
# # nova_lista = lista_animal * 3
# # print(nova_lista)
#
# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)
#
# print(min(lista_animal))
#
# if 'lobo' in lista_animal:
#     print('existe um lobo na lista!')
# else:
#     print('nao existe um lobo na lista!')
#     lista_animal.append('lobo')
#     print('Lobo adicionado a lista!')
#     print(lista_animal)
#
# # lista_animal.pop(0) # remove os valores com base nas posições
# # print(lista_animal)
#
# # lista_animal.remove('elefante')
# # print(lista_animal)

