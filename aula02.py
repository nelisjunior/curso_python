# print('a = ' + str(a) + ', b ' + str(b))
a = int(input('Entre com o valor de a: '))
b = int(input('Entre com o valor de b: '))
print('\n===== Tipo de variável =====',
      '\n{a}', type(a),
      '\n{b}', type(b))

divisao = a / b
multiplicacao = a * b
resto = a % b
soma = a + b
subtracao = a - b

print('\n====== Com string ======')
print('divisao: ' + str(divisao))

print('\n====== Com format ======')
print('soma: {soma}'
      '\nSubtração: {subtracao}'
      '\nMultiplicação: {multiplicacao}'
      '\nDivisão: {divisao}'
      '\nResto: {resto}'.format(soma=soma,
                                subtracao=subtracao,
                                multiplicacao=multiplicacao,
                                divisao=divisao,
                                resto=resto))
