#SOLID (S) -Principio de Responsabilidade Única -- SRP

"""
Significa que temos que colocar somente uma responsabilidade em um metodo, 
para assim termos facilidade na alteração de código.
"""

#Exemplo:

class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__verificar_dados(nome,idade):
            self.__armazena_dados(nome,idade)
        else:
            self.__indicar_erro

    def __verificar_dados(self, nome: str, idade: int):
        if isinstance(nome,str) and isinstance(idade,int):
            return True
        else:
            return False
    
    def __armazena_dados(self,  nome: str, idade: int):
        print('acessando banco de dados...')
        print(f'Cadastrar usuario {nome}, idade {idade}')
    
    def __indicar_erro(self)-> None:
        print('Dados inválidos')

#---------------------------------------------------------------

#SOLID (O) -Princípio Aberto / Fechado -- OCP

"""
Entradas diferentes geram ações diferentes.

Objetos ou entidades devem estar abertos para extensão,
mas fechados para modificação, ou seja, quando novos comportamentos e recursos
precisam ser adicionados no software, devemos estender e não alterar
o código fonte original.
"""

#Exemplo:

class Circo:
    def apresentar(self, apresentador:any):
        apresentador.apresentar_show()

class Malabarista:
    def apresentar_show(self):
        print('O malabarista está apresentando...')

class Palhaco:
    def apresentar_show(self):
        print('O palhaço está fazendo palhaçada...')

class Domador:
    def apresentar_show(self):
        print('O domador está domando o leão...')

circo = Circo()
malabarista = Malabarista()
palhaco = Palhaco()

circo.apresentar(palhaco) 
"""
Nesse caso seria interessante um molde para a criação dessas classes
onde seria implementado o metodo 'apresentar_show()', podendo ser feito
 por meio de uma classe abstrata

"""

#SOLID (I) - Princípio da Segregação de Interface

"""
Princípio da Segregação da Interface — Uma classe não deve ser forçada a implementar
interfaces e métodos que não irão utilizar.
Esse princípio basicamente diz que é melhor criar interfaces
mais específicas ao invés de termos uma única interface genérica.
"""

#SOLID (D) - Princípio da Inversão de Dependência

"""
Dependa de abstrações e não de implementações.

--Módulos de alto nível não devem depender de módulos de baixo nível.
  Ambos devem depender da abstração.

Um módulo de alto nível não deve depender de módulos de baixo nível,
ambos devem depender da abstração. 

Módulo de alto nível é um módulo que depende de outros módulos.
"""


