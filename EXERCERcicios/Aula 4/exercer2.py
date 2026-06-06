'''Crie uma classe Pessoa com atributos privados __nome e __idade. O setter de idade deve aceitar apenas
valores entre 0 e 120. O setter de nome deve rejeitar strings vazias. Crie um método apresentar() que
imprime os dados da pessoa.'''
class pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome 
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if not nome.strip():
            raise ValueError(" não pode vazio ")
        self.__nome = nome

    def set_idade(self, idade):
        if 0 <= idade <= 120:
            self.__idade = idade
        else:
            raise ValueError ("eta Pode ser mais véio que isso não")
        
    def apresentar(self):
            return f"Nome: {self.__nome} | Idade {self.__idade} anos? "
        

try:
    p1 = pessoa("Carlos Silva", 30)
    print(p1.apresentar())

    p2 = pessoa("", 25)

except ValueError as e:
    print(f"Erro de validação {e}")