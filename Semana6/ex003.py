

class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


def inserir(pilha, dado):
    novo = No(dado)

    if pilha is None:
        return novo

    novo.proximo = pilha
    return novo


def remover(pilha):
    if pilha is None:
        return None

    pilha = pilha.proximo
    return pilha


def main():
    pilha = None

    for i in range(1, 21):
        carro = "Carro" + str(i)
        pilha = inserir(pilha, carro)

    print("Carros na garagem cadastrados!")

    carro_saida = input("Qual carro deseja retirar? ")

    encontrado = False

    while pilha is not None:
        print("Retirando:", pilha.dado)

        if pilha.dado == carro_saida:
            encontrado = True
            pilha = remover(pilha)
            break

        pilha = remover(pilha)

    if encontrado:
        print("Carro retirado com sucesso!")
    else:
        print("Carro não encontrado na garagem.")


main()



