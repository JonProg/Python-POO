from collections import namedtuple

# namedtuples - tuplas imutáveis com nomes para valores
# Usamos namedtuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou registros de
# bases de dados, etc.
# As namedtuples são imutáveis assim como as tuplas.
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NamedTuple

# from collections import namedtuple

from typing import NamedTuple


class Pokemon(NamedTuple):
    nome: str = 'POKEMON_NAME'
    tipo: str = 'TYPE'


# Carta = namedtuple(
#     'Carta', ['valor', 'naipe'],
#     defaults=['VALOR', 'NAIPE']
# )

firt_pokemon = Pokemon('Gengar', 'shadow')

print(firt_pokemon._asdict())
print(firt_pokemon)
print(firt_pokemon[0])
print(firt_pokemon.nome)
print(firt_pokemon[1])
print(firt_pokemon.tipo)

print()
print(firt_pokemon._fields)
print(firt_pokemon._field_defaults)


for valor in firt_pokemon:
    print(valor)