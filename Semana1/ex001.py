
class Produto:
    def __init__(self, nome, preco, qtd,):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
        self.total = 0


    def calcular_total(self):
        return self.preco * self.qtd
       


uva = Produto("Uva", 10, 30)
total = uva.calcular_total()
print(total)
    

    
      








