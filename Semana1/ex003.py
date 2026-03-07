class Produto:
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    def atualizarestoque(self): 
        atualizarqtd = int(input("Digite a quantidade a atualizar: "))
        estoqueantes = self.qtd
        print("Estoque anterior:", estoqueantes)
        self.qtd += atualizarqtd


Computador = Produto("Computador ", 100, 200)
Computador.atualizarestoque()
print("Estoque novo:", Computador.qtd)

Monitor = Produto("Monitor", 20, 10)
Monitor.atualizarestoque()
print("Estoque novo:", Monitor.qtd)


