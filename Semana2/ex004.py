class No:
    def __init__(self, item):
        self.item = item
        self.proximo = None

def inserirItem(lista, item):

        novoItem = No(item)
        novoItem.proximo = lista
        lista = novoItem
        return lista


def concatena(lista1, lista2):
    aux = lista1
    aux2 = lista2
    if lista1 is None:
        print("Primeira lista vazia")
        return
    elif lista2 is None:
        print("Segunda lista vazia")
        return
    while aux.proximo is not None:
        aux = aux.proximo
    aux.proximo = lista2
    return lista1



def menu():
    print("1 - Inserir item na primeira lista")
    print("2 - Inserir item na segunda lista")
    print("3 - Concatenar")
    opc = int(input("Digite uma opção: "))
    return opc


def main():
    lista = None
    lista2 = None
    concatenacao = None
    opc = 0
    while opc != 4:
        opc = menu()
        
        if opc == 1:
            item = int(input("Digite o item para inserir: "))
            lista = inserirItem(lista, item)
        elif opc == 2:
            item = int(input("Digite o item para inserir: "))
            lista2 = inserirItem(lista2, item)
        elif opc == 3:
            concatenacao = concatena(lista, lista2)
            while concatenacao is not None:
                print(concatenacao.item)
                concatenacao = concatenacao.proximo
            

main()