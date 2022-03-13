# Aula 4: Criando laços de repetição em Python

# ================= Exercício 4.3 =================
# while: aplicação realizada no exercício 3.4 da aula 3!

a = 0
while a <= 10:
    print(a)
    a += 1


# # ================= Exercício 4.2 =================
# # FOR: Quantidade de números primos dentro de um intervalo!
#
# a = int(input('Entre com um número: '))
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         # print(x, resto)
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print(num)

# # ================= Exercício 4.1 =================
# # FOR: Verifica se é número primo!
#
# a = int(input('Entre com um número: '))
#
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(a, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('Número {} é primo!'.format(a))
# else:
#     print('Número {} não é primo!'.format(a))
