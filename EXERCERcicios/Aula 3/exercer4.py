'''Crie uma classe ContaBancaria com os atributos titular e saldo. Implemente os métodos:
• depositar(valor) – soma o valor ao saldo
• sacar(valor) – subtrai o valor do saldo, mas apenas se houver saldo suficiente. Caso contrário imprima
"Saldo insuficiente"
• extrato() – imprime o titular e o saldo atual'''

class Contabancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"o valor depositado foi de {valor:.2f}")
        else:
            print("depositou errado patrão")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"realizado sacamento de pistola {valor}")
        else:
            print("seu quebrado, transação não aceita")
    
    def extrato(self):
        print(self.titular, self.saldo)
    
Bradesco = Contabancaria("Diego Silva", 1)
Bradesco.depositar(200.0)
Bradesco.sacar(50.0)
Bradesco.extrato()
Bradesco.sacar(300.0)