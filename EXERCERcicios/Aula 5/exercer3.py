'''Crie uma classe mãe Funcionario com atributos nome e salario, e um método exibir(). Crie uma classe
lha Gerente que herda de Funcionario e adiciona o atributo bonus. Crie um método salario_total()
que retorna salário + bônus.'''
class funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def exibir(self):
        return 0
    
class gerente(funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def salario_total(self):
        return self.salario + self.bonus
    
caso = gerente("CARLOS", 3000, 750)

print(f"salario normal {caso.salario} salario poś o bonus {caso.salario_total()}")