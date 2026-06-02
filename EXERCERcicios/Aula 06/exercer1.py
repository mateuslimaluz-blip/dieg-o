"""Crie uma classe mãe Funcionario com um método calcular_salario() que retorna 0. Crie duas lhas:
Vendedor (salário xo + comissão) e Gerente (salário xo + bônus). Cada uma sobrescreve calcular_salario().
Crie um objeto de cada e imprima o salário. """

class funcionario:
    def __init__(self, nome):
        self.nome = nome

    def calcular_salario(self):
        return 0 
    
class vendedor(funcionario):
    def __init__(self, nome, salario_fixo, comissao):
        super().__init__(nome)
        self.salario_fixo = salario_fixo
        self.comissao = comissao

    def calcular_salario(self):
        return self.salario_fixo + self.comissao

class gerente(funcionario):
    def __init__(self, nome, salario_fixo, bonus):
        super().__init__(nome)
        self.salario_fixo = salario_fixo
        self.bonus = bonus

    def calcular_salario(self):
        return self.salario_fixo + self.bonus

vendedor = vendedor("carlos", 1500, 200)
gerente = gerente("juan", 2000, 500)

print(f"{vendedor.nome} tem salario de {vendedor.calcular_salario()}")
print(f"{gerente.nome} tem salario de {gerente.calcular_salario()}")