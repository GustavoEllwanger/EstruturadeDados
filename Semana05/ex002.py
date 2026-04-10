class No:
    def __init__(self, cliente):
        self.cliente = cliente
        self.proximo = None
        self.anterior = None


def adicionarCliente(lista, cliente):
    novo = No(cliente)

    if lista is None:
        novo.proximo = novo
        novo.anterior = novo
        return novo

    lista.anterior.proximo = novo
    novo.anterior = lista.anterior
    novo.proximo = lista
    lista.anterior = novo

    return lista


def removerCliente(lista, cliente):
    if lista is None:
        return lista, False

    aux = lista

    while True:
        if aux.cliente == cliente:
            if aux.proximo == aux:
                return None, True

            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior

            if aux == lista:
                lista = aux.proximo

            return lista, True

        aux = aux.proximo

        if aux == lista:
            return lista, False


def simularPizza(lista):
    if lista is None:
        print("Nao ha clientes no rodizio.")
        return

    qtd = int(input("Quantas passagens da pizza deseja simular? "))
    aux = lista

    for i in range(qtd):
        print(aux.cliente, "recebeu a fatia 🍕")
        aux = aux.proximo


def mostrarClientes(lista):
    if lista is None:
        print("Nao ha clientes no rodizio.")
        return

    aux = lista

    while True:
        print(aux.cliente)
        aux = aux.proximo

        if aux == lista:
            break


def main():
    lista = None

    while True:
        print("\n--- MENU ---")
        print("1 - Adicionar cliente")
        print("2 - Remover cliente")
        print("3 - Simular passagem da pizza")
        print("4 - Mostrar clientes")
        print("5 - Sair")

        op = int(input("Escolha uma opcao: "))

        if op == 1:
            nome = input("Digite o nome do cliente: ")
            lista = adicionarCliente(lista, nome)
            print("Cliente adicionado com sucesso.")

        elif op == 2:
            nome = input("Digite o nome do cliente que foi embora: ")
            lista, removido = removerCliente(lista, nome)

            if removido:
                print("Cliente removido com sucesso.")
            else:
                print("Cliente nao encontrado.")

        elif op == 3:
            simularPizza(lista)

        elif op == 4:
            mostrarClientes(lista)

        elif op == 5:
            print("Encerrando o programa.")
            break

        else:
            print("Opcao invalida.")


main()
