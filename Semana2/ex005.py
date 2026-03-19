class No:
    def __init__(self, item):
        self.item = item
        self.proximo = None
    

def lista_insere_final(lista, item):
     aux = lista
     novoItem = No(item)
     if lista == None:
         return novoItem
     while aux.proximo is not None:
        aux = aux.proximo
     aux.proximo = novoItem
     return lista
    

def listarItem(lista):
    aux = lista
    if aux == None:
        print("Lista vazia")
    while aux is not None:
        print("Item: ", aux.item)
        aux = aux.proximo
    return lista

def menu():
    print("1 - Inserir item")
    print("2 - Listar item")
    print("3 - Sair")
    opc = int(input("Digite uma opção: "))
    return opc


def main():
    lista = None
    opc = 0
    while opc != 4:
        opc = menu()
        if opc == 1:
            item = int(input("Digite um valor: "))
            lista = lista_insere_final(lista, item)
        elif opc == 2:
            lista = listarItem(lista)
main()