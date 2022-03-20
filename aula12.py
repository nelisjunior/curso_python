# Aula12: Pacotes do Python
# Instalando e utilizando pacotes em Python e realizar requisição com requests
# ID: gUZ8tZjeLNU
# https://viacep.com.br/
# https://pokeapi.co/
# https://globallabs.academy/

# Bibliotecas importadas

import requests

# ================= Exemplo 12.1 =================


def retorna_dados__cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    # print(response.status_code)
    # print(response.text)
    # print(response.json())
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])
    return dados_cep


def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    print(dados_pokemon['id'])
    print(dados_pokemon['name'])
    print(dados_pokemon['base_experience'])
    print(dados_pokemon['sprites']['front_shiny'])
    return dados_pokemon


def retorna_response(url):
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    # response = retorna_response('https://globallabs.academy/')
    # print(response)
    retorna_dados_pokemon('pikachu')
    # dados_pokemon = retorna_dados_pokemon('pikachu')
    # print(dados_pokemon)
    # retorna_dados__cep('22041001')
