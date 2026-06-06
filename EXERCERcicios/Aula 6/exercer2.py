"""Crie uma classe mãe Instrumento com método tocar(). Crie três lhas: Violao, Bateria e Piano, cada
uma sobrescrevendo tocar() com um som diferente. Crie uma lista com os três e percorra chamando tocar()
de cada um."""
class Instrumento:
    def __init__(self, som):
        self.som = som

    def tocar(self):
        return ("SOM GENERIC")
    
class Violao(Instrumento):
    def __init__(self, som):
        super().__init__(som)

    def tocar(self):
        return f"BRUM BRUMMM"
    
class Bateria(Instrumento):
    def __init__(self, som):
        super().__init__(som)

    def tocar(self):
        return f"TUM TUM TUM ({self.som})"
    
class Piano(Instrumento):
    def __init__(self, som):
        super().__init__(som)

    def tocar(self):
        return f"*SOM DE PIANOS* ({self.som})"
    
Instruir = [ 
    Violao("Viola"),
    Bateria("tambor"),
    Piano("Piano👍") 
]
for Instrumento in Instruir:
    print(f"{Instrumento.som}: {Instrumento.tocar()}")