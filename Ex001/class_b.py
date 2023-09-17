import json

from class_a import CAMINHO_ARQUIVO, Pokemons

def ler_dados():
    with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
        pokemon = json.load(arquivo)

    p1 = Pokemons(**pokemon[0])
    p2 = Pokemons(**pokemon[1])
    p3 = Pokemons(**pokemon[2])

    return f'{p1.nome} -- {p1.tipo}\n{p2.nome} -- {p2.tipo}\n{p3.nome} -- {p3.tipo}'

if __name__ == '__main__':
    print(ler_dados())