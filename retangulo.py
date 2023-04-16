class retangulo():
    def __init__(self, altura, lagura):
        self.altura = altura 
        self.largura = lagura

    def calcular_area(self):
        area = self.altura * self.largura
        return f" O valor da area e {area}"
    
    def imprimir(self):
        print(f" Altura: {self.altura}")
        print(f" largura: {self.largura}")

r = retangulo(5,40)
print(r.calcular_area())
r.imprimir()

        
         