from random import randint

class No:
    def __init__(self, guerreiro):
        self.guerreiro = guerreiro
        self.proximo = None
        self.anterior = None


def adicionarGuerreiro(lista, guerreiro):
    novo = No(guerreiro)

    if lista is None:
        novo.proximo = novo
        novo.anterior = novo
        return novo

    lista.anterior.proximo = novo
    novo.anterior = lista.anterior
    novo.proximo = lista
    lista.anterior = novo

    return lista


def removerGuerreiro(lista, guerreiro):
    if lista is None:
        return None

    aux = lista

    while True:
        if aux.guerreiro == guerreiro:
            if aux.proximo == aux:
                return None

            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior

            if aux == lista:
                lista = aux.proximo

            return lista

        aux = aux.proximo

        if aux == lista:
            return lista


def contarGuerreiros(lista):
    if lista is None:
        return 0

    cont = 1
    aux = lista.proximo

    while aux != lista:
        cont += 1
        aux = aux.proximo

    return cont


def simularJogo(lista):
    while contarGuerreiros(lista) > 1:
        total = contarGuerreiros(lista)
        sorteado = randint(1, total)

        aux = lista
        for i in range(1, sorteado):
            aux = aux.proximo

        print(aux.guerreiro, "foi eliminado")
        lista = removerGuerreiro(lista, aux.guerreiro)

    print("Sobrevivente:", lista.guerreiro)


def main():
    lista = None
    qtd = int(input("Digite a quantidade de guerreiros: "))

    for i in range(1, qtd + 1):
        lista = adicionarGuerreiro(lista, f"Guerreiro {i}")

    simularJogo(lista)


main()
