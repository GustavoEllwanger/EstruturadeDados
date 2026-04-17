



class No:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None

def menu():
    print("1 - Inserir operação")
    print("2 - Retirar operação (POP)")
    print("3 - Mostrar topo")
    print("4 - Mostrar pilha")
    print("5 - Sair")
    opcao = int(input("Digite a opção: "))
    return opcao

def inserir(pilha, dado):
    novo = No(dado)

    if pilha is None:
        return novo

    novo.proximo = pilha
    pilha.anterior = novo
    return novo

def remover(pilha):
    if pilha is None:
        print("Pilha vazia")
        return None

    print("Removido:", pilha.dado)

    if pilha.proximo is None:
        return None

    pilha = pilha.proximo
    pilha.anterior = None
    return pilha

def mostrar_topo(pilha):
    if pilha is None:
        print("Pilha vazia")
    else:
        print("Topo:", pilha.dado)

def mostrar_pilha(pilha):
    if pilha is None:
        print("Pilha vazia")
        return

    aux = pilha
    while aux is not None:
        print("-", aux.dado)
        aux = aux.proximo

def main():
    pilha = None
    opcao = 0

    while opcao != 5:
        opcao = menu()

        if opcao == 1:
            dado = input("Digite a operação: ")
            pilha = inserir(pilha, dado)

        elif opcao == 2:
            pilha = remover(pilha)

        elif opcao == 3:
            mostrar_topo(pilha)

        elif opcao == 4:
            mostrar_pilha(pilha)

        elif opcao == 5:
            print("Saindo...")

        else:
            print("Opção inválida")

main()



