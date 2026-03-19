class No:
    def __init__(self, item):
        self.item = item
        self.proximo = None



def inserirItem(lista, item):
    novoItem = No(item)
    novoItem.proximo = lista
    lista = novoItem
    return lista

def listarItens(lista):
    aux = lista
    if aux == None:
        (print("Lista vazia"))
        return

    while aux is not None:
        print("Item: ", aux.item)
        aux = aux.proximo




def excluirItem(lista, item):
    aux = lista
    anterior = None


    if lista is None:
        print("Lista vazia")
        return
    

    while aux is not None:
        if aux.item == item:
            if lista == aux:
                lista = lista.proximo
                return lista
            
            elif aux.proximo == None:
                anterior.proximo = None
                return lista
            

            else: 
                anterior.proximo == aux.proximo
                return lista

        else:
            anterior = aux
            aux = aux.proximo
    print("Elemento não encontrado")
    return lista


def maiores(lista, n):
    contador = 0
    aux = lista
    while aux is not None:
        if aux.item > n:
            contador += 1
            aux = aux.proximo
        else:
            aux = aux.proximo
    print("Número de nós da lista maiores que o número informado: ", contador)
    return lista
    





def menu():
    print("1 - Inserir item")
    print("2 - Listar item")
    print("3 - Excluir item")
    print("4 - Número Nós")
    print("5 - Sair")
    opc = int(input("Digite uma opção: "))
    return opc



def main():
    lista = None
    opc = 0

    while opc != 5:
        opc = menu()

        if opc == 1:
            item = int(input("Digite um item para inserir: "))
            lista = inserirItem(lista, item)
        elif opc == 2:
            listarItens(lista)
        elif opc == 3:
            item = int(input("Digite um item para excluir: "))
            lista = excluirItem(lista, item)
        elif opc == 4:
            n = int(input("Digite um número: "))
            lista = maiores(lista, n)
main()