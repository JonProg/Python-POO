from pathlib import Path
import json

CAMINHO_ARQUIVO = Path(__file__).parent / 'dados.json'

class Pokemons:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

p1 = Pokemons('cindarece', 'metal')
p2 = Pokemons('charizard', 'fogo')
p3 = Pokemons('blastoise','agua')
atributos = [vars(p1), vars(p2), vars(p3)]

def fazer_dump(): 
    with CAMINHO_ARQUIVO.open('w+', encoding='utf8') as arquivo:
        json.dump(atributos,arquivo, indent=2)
    
if __name__ == '__main__': #Ele só vai executar a função fazer_dump() somente quando este arquivo for excutado
    fazer_dump()

"""
|
Essa condicional é usado quando você quer que determinada coisa seja executada
somente quando o modulo que tem a condicional for excutado.
"""
