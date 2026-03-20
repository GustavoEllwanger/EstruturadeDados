class No:
    def __init__(self, item):
        self.item = item
        self.proximo = None




lista = No(10)
lista.proximo = No(-35)
lista.proximo.proximo = No(20)
lista.proximo.proximo.proximo = No(-50)


def lista_altera(lista):
    aux = lista
    while aux is not None:
        aux.item *= -1
        aux = aux.proximo
    return lista









def main():
    lista_final = lista_altera(lista)
    while lista_final is not None:
     print(lista_final.item)
     lista_final = lista_final.proximo


main()