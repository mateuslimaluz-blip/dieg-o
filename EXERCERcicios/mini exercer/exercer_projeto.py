class funcionario:
    def __init__(self, Nome, Matricula, Salario):
        self.Nome = Nome 
        self.__Matricula = Matricula
        self.Salario = Salario
    
    def calcular_salario(self):
        return 0
        
    def exibir(self):
        print(
            f"Nome {self.Nome}  "
            f"Matricula {self.Matricula:03d}  "
            f"Tipo {self.__class__.__name__}  "
            f"Salario R$ {self.calcular_salario():.2f}"
        )

    @property
    def Matricula(self):
        return self.__Matricula
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, valor):
        if valor <= 0 :
            raise ValueError ("não pode ser negativo ")
        
        self.__salario = self.valor
 
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


            
funcionarios = [
 CLT("Jão", 1, 1550),
 Vendedor("Pão", 2, 2500, 0.10),
 Gerente("Claudio", 3, 3000, 750)
]
for funcionario in funcionarios:
    funcionario.exibir()

"""Nome : Ana | Matricula : 001 | Tipo : CLT | Salario : R$ 3000.00"""
"""ETA"""
