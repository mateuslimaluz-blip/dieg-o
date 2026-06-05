class funcionario:
    def __init__(self, Nome, Matricula, Salario):
        self.Nome = Nome 
        self.Matricula = Matricula
        self.Salario = Salario
    
    def calcular_salario(self):
        return 0

class CLT(funcionario):
    def __init__(self, Nome, Matricula, Salario):
        super().__init__(Nome, Matricula, Salario)

    def calcular_salario(self):
        return self.Salario

class Vendedor(funcionario):
    def __init__(self, Nome, Matricula, Salario, comissao):
        super().__init__(Nome, Matricula, Salario)
        self.comissao = comissao

    def calcular_salario(self):
        return self.Salario + (self.Salario * self.comissao)
    
class Gerente(funcionario):
    def __init__(self, Nome, Matricula, Salario, bonus):
        super().__init__(Nome, Matricula, Salario)
        self.bonus = bonus

    def calcular_salario(self):
        return self.Salario + self.bonus

trabalhador = CLT("Jão", 1, 1550)
trabalhador2 = Vendedor("Pão", 2, 2500, 0.10)
trabalhador3 = Gerente("Claudio", 3, 3000, 750)

print(f"Nome : {trabalhador.Nome} | Matricula : {trabalhador.Matricula: 04d} | Tipo : CLT | Salario : R$ {trabalhador.calcular_salario():.2f}")
print(f"Nome : {trabalhador2.Nome} | Matricula : {trabalhador2.Matricula: 04d} | Tipo : Vendedor | Salario : R$ {trabalhador2.calcular_salario():.2f}")
print(f"Nome : {trabalhador3.Nome} | Matricula : {trabalhador3.Matricula: 04d} | Tipo : Gerente | Salario : R$ {trabalhador3.calcular_salario():.2f}")

"""Nome : Ana | Matricula : 001 | Tipo : CLT | Salario : R$ 3000.00"""