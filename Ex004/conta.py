from abc import ABC, abstractmethod

autorizado = False

class Conta(ABC):

    def __init__(self, agencia: int, conta: int, saldo: float = 0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        

    @abstractmethod
    def sacar(self, valor: float) -> float:...

    def depositar(self, valor: float):
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO {valor})')
    
    def detalhes(self, msg =''):
        print("-"*25)
        print(f'O seu saldo é {self.saldo:.2f} {msg}')


class ContaCorrente(Conta):

    def __init__(self, agencia, conta, saldo=0, limite=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        if autorizado == True:
            if valor_pos_saque >= -self.limite:
                self.saldo -= valor
                return self.detalhes(f'(SAQUE {valor})')

            return self.detalhes(f'(SAQUE NEGADO {valor})')
        else:
            print("Você não está autorizado")
         

class ContaPoupanca(Conta):

    def sacar(self, valor):
        if autorizado == True:
            if valor <= self.saldo:
                self.saldo -= valor
                return self.detalhes(f'(SAQUE {valor})')

            return self.detalhes(f'(SAQUE NEGADO {valor})')
        else:
            print("Você não está autorizado")
            
if __name__ == "__main__":
    cp1 = ContaCorrente(11,222,300,100)
    print(type(cp1).__name__ == "ContaCorrente")
    