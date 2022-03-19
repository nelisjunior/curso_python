# Aula 08: Lidando com módulos
# Importação de classes, métodos e construção de funções anônimas(lambda)

# ================= Exemplo 8.2 =================
# Método contador de palavras

def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador


def teste():
    return 'teste'


if __name__ == '__main__':
    lista = ['cachorro', 'gato']
    print(contador_letras(lista))
