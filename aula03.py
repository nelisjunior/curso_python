# Aula 3: Como criar um código que funcione de acordo com a relação das variáveis

#  ================= Exercicio 3.4 =================
a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Você digitou errado. Tente novamente! \nPrimeiro bimestre: '))

b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('Você digitou errado. Tente novamente! \nSegundo bimestre: '))

c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Você digitou errado. Tente novamente! \nTerceiro bimestre: '))

d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('Você digitou errado. Tente novamente! \nQuarto bimestre: '))

media = (a + b + c + d)/4

print('Sua média é: ', int(media))


# #  ================= Exercicio 3.3 =================
# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2
#
#
# if resto_a == 0 or not resto_b > 0:
#     print('Ao menos um número par foi digitado!')
# else:
#     print('Nenhum número par foi digitado!')


# #  ================= Exercicio 3.2 =================
# a = int(input('Entre com um valor: '))
# resto = a % 2
#
# if resto == 0:
#     print(a, 'é par')
# else:
#     print(a, 'é impar')

# # ================= Exercicio 3.1 =================
# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
# if a > b:
#     print('o maior número é {}'.format(a))
# elif b > a and b > c:
#     print('o maior número é {}'.format(b))
# else:
#     print('o maior número é {}'.format(c))
# print('Final do programa')
