class Lista:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

def inserirItem(lista, dado):
    novo = Lista(dado)
    novo.proximo = lista
    return novo
    



def listarItem(lista):
    atual = lista

    while atual is not None:
        print("- ", atual.dado)
        atual = atual.proximo


def removerItem(lista,dado):
    if lista is None:
        print("Lista vazia!")
        return None
    
    atual = lista
    anterior = None
    while atual is not None:
        if atual.dado == dado:

            if anterior == None:
                print("Retirado o primeiro item da lista")
                return atual.proximo
            elif atual.proximo == None:
                print("Retirado o último elemento da lista")
                anterior.proximo = None
                return lista
            else:
                anterior.proximo = atual.proximo
                print("Retirado o elemento do meio")
                return lista
        anterior = atual
        atual = atual.proximo
    print("Elemento não encontrado")
    return lista

    

def menu():
    print("1 - Inserir elemento")
    print("2 - Listar elemento")
    print("3 - Remover elemento")
    print("4 - Sair")
    opc = int(input("Digite a opção: "))
    return opc





def main():
    lista = None
    opc = 0
    
    while opc != 4:
        opc = menu()
        if opc == 1:
            try:
                dado = float(input("Digite um valor float: "))
            except:
                print("Valor inválido")
                continue
            lista = inserirItem(lista, dado)
        elif opc == 2: 
            listarItem(lista)          
        elif opc == 3:
            try:
                dado = float(input("Digite o item que quer remover "))
            except:
                print("Valor inválido")
                continue
            lista = removerItem(lista,dado)


main()