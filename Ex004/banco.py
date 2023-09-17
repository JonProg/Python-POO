import conta
from pessoas import Cliente


class Banco:

    def __init__(self):
        self.__clientes = ["jonas", "samuel", "dandara"]
        self.__contas = ["ContaCorrente","ContaPoupanca"]
        self.__agencias = [123,456,678,900]

    
    def autenticar(self, cliente: Cliente, conta: conta.Conta):
        condicao = conta.agencia in self.__agencias and type(conta).__name__ in self.__contas
        return True if condicao and cliente.nome in self.__clientes else False




