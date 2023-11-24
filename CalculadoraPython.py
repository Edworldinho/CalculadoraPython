class CalculadoraPython:
    
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b

    def somar(self,a,b):
        return self.a + self.b
    
    def diminuir(self,a,b):
        return self.a - self.b
    
    def multiplicar(self,a,b):
        return self.a * self.b
    
    def dividir(self,a,b):
        return self.a / self.b
