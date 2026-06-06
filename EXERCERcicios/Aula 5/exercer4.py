'''Crie uma classe mãe Pessoa com atributos nome e idade. Crie duas lhas: Aluno (com atributo matricula) e
Professor (com atributo salario). Cada lha deve ter um método apresentar() próprio que mostre todos
os seus dados. Crie uma lista contendo objetos das duas classes e percorra com for chamando apresentar()
de cada um.'''
class pessoa:
    def __init__(self, idade, nome):
        self.nome = nome
        self.idade = idade

class aluno(pessoa):
    def __init__(self, idade, nome, matricula):
        super().__init__(idade, nome)
        self.matricula = matricula

    def apresentar(self):
        return "I am ALUNOS", self.nome
    
class professor(pessoa):
    def __init__(self, idade, nome, salario):
        super().__init__(idade, nome)
        self.salario = salario

    def apresentar(self):
        return "I am professor ", self.nome
    
people = [
    aluno(17, "Mateus", 777),
    professor(28, "Diego", 666)
]

for pessoa in people:
    print(f"{pessoa.apresentar()}")