class No:
    def __init__(self, item):
        self.item = item
        self.proximo = None


    
lista = No(10)
lista.proximo = No(20)
lista.proximo.proximo = No(30)


def lista_calcula_media(lista):
     contador = 0
     soma = 0
     aux = lista
     if lista == None:
         print("Lista vazia!")
         return
     while aux is not None:
        contador += 1
        soma += aux.item
        aux = aux.proximo
     media_final = soma / contador
     return media_final
        


def main():
    resultado = lista_calcula_media(lista)
    print(resultado)
main()
