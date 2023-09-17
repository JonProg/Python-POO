class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):#Esse aqui simplismente exibe o objeto como uma str
        return f'({self.x}, {self.y})'

    def __repr__(self): #É uma comunicação de como você quer que esse objeto seja criado
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'
        #!r para mostrar a representaçâo do paremetro

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)
    
    def __gt__(self, other):
        resultado_self= self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other

    

p1 = Ponto(1, 2)
p2 = Ponto(978, 876)
p3 = p1+p2
print(p1)
print(repr(p2))
print(f'{p2!r}')
print(p3)
print('P1 é maior que p2', p1>p2)
print('P2 é maior que p1', p2>p1)

#------------------------------------------------------

