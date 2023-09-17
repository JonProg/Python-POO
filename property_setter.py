""" 
@property - um getter no modo Pythônico
getter - um método para obter um atributo
cor -> get_cor()
modo pythônico - modo do Python de fazer coisas
@property é uma propriedade do objeto, ela
é um método que se comporta como um atributo 
Geralmente é usada nas seguintes situações:
 - como getter
 - p/ evitar quebrar código cliente
 - p/ habilitar setter
 - p/ executar ações ao obter um atributo
 
Código cliente - é o código que usa seu código
"""

class Caneta1:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta

    @property
    def cor_tampa(self):
        return 123456


caneta = Caneta1('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)

#------------------------------

""" 
- usamos o  getter
- p/ evitar quebrar código cliente
- p/ habilitar setter
- p/ executar ações ao obter um atributo
Atributos que começar com um ou dois underlines
não devem ser usados fora da classe.
"""


class Caneta2:
    def __init__(self, cor):
        # private protected
        self.cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        print('ESTOU NO GETTER')
        return self._cor

    @cor.setter
    def cor(self, valor):
        print('ESTOU NO SETTER')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta2('Azul')
caneta.cor = 'Rosa'
caneta.cor_tampa = 'Azul'
print(caneta.cor)
print(caneta.cor_tampa)

