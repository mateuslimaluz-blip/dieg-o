'''Crie uma classe mãe Forma com método area(). Crie as lhas Triangulo (base e altura) e Quadrado (lado),
cada uma calculando sua própria área. Crie uma lista com várias formas e imprima a área de cada uma.'''
class forma:
    def __init__(self):
    
     def area(self):
        return 0
    
class triangulo(forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
       return self.base * self.altura / 2
    
class quadrado(forma):
    def __init__(self, lado):
      self.lado = lado

    def area(self):
      return self.lado * self.lado
    
formas = [
   triangulo(10, 10),
   quadrado(30),
   triangulo(25, 12.5),
   quadrado(32.2)
]

for forma in formas:
   print(f"formas: {type(forma).__name__} | Área: {forma.area()}")