# Aula11:
# Gerenciando e criando exceções customizadas com try, except, else e finally
# Exceções embutidas: https://docs.python.org/pt-br/3/library/exceptions.html#exception-hierarchy
# ID: KoCz2L23JLw

# ================= Exemplo 11.1 =================

lista = [1, 10]

try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]

except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0!')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritmética')
except IndexError:
    print('Error ao acessar um indice inválido da lista')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre exceção')
finally:
    print("Sempre executa:")
    print('Fechando arquivo...')
    arquivo.close()
    print('Arquivo fechado!')

