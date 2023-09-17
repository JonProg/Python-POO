#--------------------------------------------------

# Métodos em instâncias de classes Python
# Hard coded - É algo que foi escrito diretamente no código
class Carro:
    def __init__(self, nome): #self = é a instancia da classe (objeto) 
        self.nome = nome
    

    def acelerar(self):
        print(f'{self.nome} está acelerando...')


#Aqui temos um metodo que é simplismente uma função 
#que receba como o primeiro valor 
#self que a minha instancia


string = 'Luiz'
print(string.upper())

fusca = Carro('Fusca') #fusca é o objeto da classe ou instancia se preferir
print(fusca.nome)
fusca.acelerar() 

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()

#--------------------------------------------------

#@classmethod

# Métodos de classe + factories (fábricas) por conta de criar uma nova instancia apartir de uma classe
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)


p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa('Anônima', 23)
p4 = Pessoa.criar_sem_nome(25)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)

#--------------------------------------------------

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls() #connection == self
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def log(msg):
        print('LOG:', msg)


def connection_log(msg):
    print('LOG:', msg)


# c1 = Connection()
c1 = Connection.create_with_auth('luiz', '1234')
print(Connection.log('Essa é a mensagem de log'))
print(c1.user)
print(c1.password)

#--------------------------------------------------

