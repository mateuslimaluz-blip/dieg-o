'''Crie uma classe ContaBancaria com atributos privados __titular e __saldo (saldo inicia em 0). Imple-
mente:

• depositar(valor) – só aceita valores positivos
• sacar(valor) – só aceita se houver saldo suficiente
• get_saldo() – retorna o saldo atual
• extrato() – imprime titular e saldo'''

class ContaBancaria:
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"valor {valor:.2f} depositado com succes ")
        else:
            print("Deve ser valor positivo")

    def sacar(self, valor):
        if valor < 0:
            print("O saque deve ser positivo")
        elif valor > self.__saldo:
            print("Voce não tem tudo isso ")
        else: 
            self.__saldo -= valor
            print(f"saque de {valor:.2f} acabou de ocorrer") 

    def get_saldo(self):
        return self.__saldo
    
    def extrato(self):
        print(f"Titular {self.__titular}")
        print(f"Saldo R$ {self.__saldo:.2f}")

if __name__ == "__main__":
        Minha_conta = ContaBancaria("Mateus Limão")

        Minha_conta.extrato()

        Minha_conta.depositar(5000.99)
        Minha_conta.depositar(-990)

        Minha_conta.sacar(5.32)
        Minha_conta.sacar(6000.99)

        Minha_conta.extrato()