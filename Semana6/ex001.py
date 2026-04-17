

class No:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None

def menu():
    print("1 - Adicionar jogador")
    print("2 - Remover jogador específico")
    print("3 - Simular 1 rodada")
    print("4 - Simular N rodadas")
    print("5 - Mostrar fila")
    print("6 - Mostrar próximo a jogar")
    print("7 - Limpar fila")
    print("8 - Sair")
    return int(input("Digite a opção: "))


def inserir_dado(fila, fim_fila, dado):
    novo = No(dado)

    if fila is None:
        return novo, novo

    fim_fila.proximo = novo
    novo.anterior = fim_fila
    return fila, novo


def retirar_inicio(fila, fim_fila):
    if fila is None:
        return None, None, None

    removido = fila.dado

    if fila == fim_fila:
        return None, None, removido

    fila = fila.proximo
    fila.anterior = None
    return fila, fim_fila, removido


def remover_especifico(fila, fim_fila, nome):
    aux = fila

    while aux is not None:
        if aux.dado == nome:
            print("Removendo:", aux.dado)

            if aux == fila:
                return retirar_inicio(fila, fim_fila)[:2]

            if aux == fim_fila:
                fim_fila = aux.anterior
                fim_fila.proximo = None
                return fila, fim_fila

            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior
            return fila, fim_fila

        aux = aux.proximo

    print("Jogador não encontrado")
    return fila, fim_fila


def mostrar_fila(fila):
    if fila is None:
        print("Fila vazia")
        return

    aux = fila
    print("Fila:")
    while aux is not None:
        print("-", aux.dado)
        aux = aux.proximo


def mostrar_frente(fila):
    if fila is None:
        print("Fila vazia")
    else:
        print("Próximo a jogar:", fila.dado)


def simular_rodada(fila, fim_fila):
    fila, fim_fila, jogador = retirar_inicio(fila, fim_fila)

    if jogador is None:
        print("Fila vazia")
        return fila, fim_fila

    print("Jogou:", jogador)

    fila, fim_fila = inserir_dado(fila, fim_fila, jogador)
    return fila, fim_fila


def simular_n_rodadas(fila, fim_fila, n):
    for i in range(n):
        print("\nRodada", i + 1)
        fila, fim_fila = simular_rodada(fila, fim_fila)
        mostrar_fila(fila)

    return fila, fim_fila


def limpar_fila():
    return None, None


def main():
    fila = None
    fim_fila = None

    while True:
        opcao = menu()

        if opcao == 1:
            nome = input("Nome do jogador: ")
            fila, fim_fila = inserir_dado(fila, fim_fila, nome)

        elif opcao == 2:
            nome = input("Nome para remover: ")
            fila, fim_fila = remover_especifico(fila, fim_fila, nome)

        elif opcao == 3:
            fila, fim_fila = simular_rodada(fila, fim_fila)

        elif opcao == 4:
            n = int(input("Quantas rodadas: "))
            fila, fim_fila = simular_n_rodadas(fila, fim_fila, n)

        elif opcao == 5:
            mostrar_fila(fila)

        elif opcao == 6:
            mostrar_frente(fila)

        elif opcao == 7:
            fila, fim_fila = limpar_fila()
            print("Fila limpa")

        elif opcao == 8:
            print("Saindo...")
            break

        else:
            print("Opção inválida")


main()



