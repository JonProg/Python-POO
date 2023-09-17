"""
Classes abstratas - Abstract Base Class (abc)
ABCs são usadas como contratos para a definição
de novas classes. Elas podem forçar outras classes
a criarem métodos concretos. Também podem ter
métodos concretos por elas mesmas.
@abstractmethods são métodos que não têm corpo.
As regras para classes abstratas com métodos
abstratos é que elas NÃO PODEM ser instânciadas
diretamente.
Métodos abstratos DEVEM ser implementados
nas subclasses (@abstractmethod).
Uma classe abstrata em Python tem sua metaclasse
sendo ABCMeta.
É possível criar @property @setter @classmethod
@staticmethod e @method como abstratos, para isso
use @abstractmethod como decorator mais interno."""


from abc import ABC, abstractmethod

class Log(ABC):
    @abstractmethod
    def _log(self, msg):...

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

l1 = LogPrintMixin()
l1.log_success('Que legal')

#--------------------------------------------------------

# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.

from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    @abstractmethod
    def name(self, name): ...


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        # print('Sou inútil')

    @AbstractFoo.name.setter
    #O 'AbstractFoo' é o namespace da classe que nesse caso está servindo para derecionar
    #a property do setter 'name' já que o mesmo está dentro da classe
    def name(self, name:str):
        self._name = name.capitalize()


foo = Foo('Bar')
foo.name = 'jonas'
print(foo.name)




