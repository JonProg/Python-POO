import conta

class Pessoa:

    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome.lower()
        self.idade = idade

class Cliente(Pessoa):
    
    def tipo_conta(self, conta: conta.Conta):
        print(f'Agencia: {conta.agencia}')
        print(f'Saldo: {conta.saldo}')