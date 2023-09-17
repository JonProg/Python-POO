class A:
    def __new__(cls, *args, **kwargs): 
        instancia = super().__new__(cls)# Criando a instancia...
        return instancia#Retornando a instancia para o self do __init__

    def __init__(self, x):
        self.x = x
        print('Sou o init')

    def __repr__(self):
        return 'A()'


a = A(123)
print(a.x)