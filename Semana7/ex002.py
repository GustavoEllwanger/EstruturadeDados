class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None



def adicionar_inicio(dado, lista):
    novo = No(dado)
    if lista is None:
        return novo
    novo.proximo = lista
    lista.anterior = novo
    
    return novo



def percorrer_lista(lista):
    aux = lista

    while aux is not None:
        print(aux.dado)
        aux = aux.proximo



def percorrer_trás(lista):

    aux = lista

    while aux.proximo is not None:
        aux = aux.proximo

    while aux is not None:
        print(aux.dado)
        aux = aux.anterior



def menu():
    print("1 - Adicionar início")
    print("2 - percorrer ")
    print("3 - percorrer trás")
    print("4 - Sair")
    opc = int(input("Digite a opção:"))
    return opc




def main():
    lista = None
    opc = 0

    while opc != 4:
        opc = menu()

        if opc == 1:
            dado = int(input("Digite o dado: "))
            lista = adicionar_inicio(dado, lista)
        elif opc == 2:
            percorrer_lista(lista)
        elif opc == 3:
            percorrer_trás(lista)

main()
