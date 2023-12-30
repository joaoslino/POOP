class Retangulo:

    is_square = False

    def __init__(self, largura, comprimento):
        self.largura = largura
        self.comprimento = comprimento

    def check_values(self):
        if (self.largura <= 0 | self.largura > 20):
            self.largura = 1
            
        if (self.comprimento <= 0 | self.comprimento > 20):
            self.comprimento = 1

        print(self.largura)
        print(self.comprimento)
         
    def perimetro(self):
        self.check_values()
        return 2*self.largura +2*self.comprimento
    
    def area(self):
        self.check_values() 
        return self.largura*self.comprimento

    def check_square(self):
        self.check_values()
        if(self.largura == self.comprimento):
           self.is_square = True
        return self.is_square
    
    def info_retangulo(self):
        area = self.area()
        perimetro = self.perimetro()
        return print(f"Largura: {self.largura}\nComprimento: {self.comprimento}\nArea: {area}\nPerimetro: {perimetro}\nQuadrado: {self.is_square}")


r1 = Retangulo(2, 3)
r1.info_retangulo()