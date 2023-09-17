"""
Todas as relações entre objetos falam que um objeto conversa com outro objeto.
Só que, dependendo da força dessa conversa e dependendo de do ciclo de vida do objeto,
ou seja, se um objeto gerencia o ciclo de vida de outro objeto, você está falando em composição.
Se um objeto precisa de outro objeto, você está falando em agregação.
E se um objeto se comunica com outro objeto, você está falando em uma associação simples."""

#Associação Simples
class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        print(f'{self.nome}')
        self._ferramenta = ferramenta


class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'


escritor = Escritor('Luiz')
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Máquina')

print(caneta.escrever())
escritor.ferramenta = maquina_de_escrever
print(maquina_de_escrever.escrever())

"""
Uma associação define um relacionamento entre duas classes
que permite que um objeto faça com que outro objeto realize uma ação em seu lugar.
Em termos gerais, a casualidade da ação é feita ao enviar
uma mensagem ou invocar um método do objeto controlado.

"""
print(escritor.ferramenta.escrever())

#------------------------------------------

#Agregação

"""
Agregação é uma forma mais especializada de associação
entre dois ou mais objetos. 
Cada objeto terá seu ciclo de vida independente.
Geralmente é uma relação de um para muitos, onde um
objeto tem um ou muitos objetos.
Os objetos podem viver separadamente, mas pode
se tratar de uma relação onde um objeto precisa de
outro para fazer determinada tarefa.
(existem controvérsias sobre as definições de agregação).
"""

class Carrinho:

    def __init__(self):
        self._produtos = []

    def total(self):
        return f'R${sum(p.preco for p in self._produtos)}'.replace('.',',')

    def inserir_produtos(self, *produtos):
        # self._produtos.extend(produtos)
        # self._produtos += produtos
        for produto in produtos: #--produto-- é o meu objeto
            self._produtos.append(produto)

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())

#------------------------------------------

#Composição

# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero)) #A instancia da classe Endereco é criada na classe Cliente

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('APAGANDO,', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO,', self.rua, self.numero)


cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av Brasil', 54)
cliente1.inserir_endereco('Rua B', 6745)

endereco_externo = Endereco('Av Saudade', 123213) 
"""
Como essa instacia não esta associada com a classe Cliente
ele não é excluida quando o cliente é excluido"""

cliente1.inserir_endereco_externo(endereco_externo)
cliente1.listar_enderecos()

del cliente1

print(endereco_externo.rua, endereco_externo.numero)
print('-------AQUI TERMINA MEU CÓDIGO-------')

#-----------------------------------------

#Herança

"""
Herança simples - Relações entre classes
Associação - usa, Agregação - tem
Composição - É dono de, Herança - É um

Herança vs Composição(Agrega a associação e a agregação)

Classe principal (Pessoa)
   -> super class, base class, parent class
Classes filhas (Cliente)
   -> sub class, child class, derived class
"""

class Pessoa():
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def falar_nome_classe(self):
        print('Classe Pessoa')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente01(Pessoa):
    def falar_nome_classe(self):
        print('Primeiro é cliente')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Aluno(Pessoa):
    ...

c1 = Cliente01('Jonas', 'Henrique')
a1 = Aluno('Gabriel', 'Joestar')

c1.falar_nome_classe()
a1.falar_nome_classe()


