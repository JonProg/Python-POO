class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor.nome

    @property
    def fabricante(self):
        return self._motor
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante.nome
    
    def especificacoes(self):
        return f'Nome:{self.nome}\nMotor:{self._motor}\nFabricante:{self._fabricante}'

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

car01 = Carro('Urus')
motor01 = Motor('ferrari')
vol = Fabricante('epaa')
car01.motor = motor01
car01.fabricante = vol

print(car01.especificacoes())


