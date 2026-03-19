class No:
    def __init__(self, item):
        self.item = item
        self.proximo = None


def inserirItem(lista, item):
    novoItem = No(item)
    novoItem.proximo = lista
    lista = novoItem
    return lista

def menu():
    print("1 - Inserir item")
    print("2 - Ultimo nó")
    opc = int(input("Digite uma opção: "))
    return opc


def ultimo(lista):
    aux = lista
    while aux.proximo is not None:
        aux = aux.proximo
    return aux
        
    


def main():
    lista = None
    ultnumero = None
    opc = 0

    while opc != 2:
        opc = menu()
        if opc == 1:
            item = int(input("Digite um item para inserir: "))
            lista = inserirItem(lista, item)
        elif opc == 2:
            ultnumero = ultimo(lista)
            if ultnumero is not None:
                print(ultnumero.item)
            else:
                print("Lista vazia")



main()