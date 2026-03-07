
class Produto:
    def __init__(self, nome, preco, qtd,):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
        self.total = 0


    def calcular_total(self):
        self.total = self.preco * self.qtd
        print("Total do produto", self.total)


uva = Produto("Uva", 10, 30)
uva.calcular_total()
    

    
      







