class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
    



def adicionar_inicio (dado, lista):

    novo = No(dado)

    if lista is None:

        lista = novo
        return lista
    
    novo.proximo = lista
    lista = novo
    return lista



def percorrer_lista(lista):
    aux = lista
    while aux is not None:
        print(aux.dado)
        aux = aux.proximo


def adicionar_final (dado, lista):

    novo  = No(dado)
    aux = lista
    if lista is None:
        return novo
    
    while aux.proximo is not None:
        aux = aux.proximo
    
    aux.proximo = novo
    return lista



def media_valor(lista):
    contador = 0
    soma = 0
    if lista is None:
        print("Lista vazia!")
        return None
    
    while lista is not None:
        contador += 1
        soma += lista.dado
        lista = lista.proximo
    
    print(soma/contador)
    return

    






    
def menu():
    print("1 Adicionar início")
    print("2 Percorrer lista")
    print("3 Adicionar no final")
    print("4 Média dos valores")
    print("5 Sair")
    opc = int(input("Digite a opção: "))
    return opc




def main():
    lista = None
    opc = 0

    while opc != 5:
        opc = menu()

        
        if opc == 1:
            dado = int(input("Digite um valor: "))
            lista = adicionar_inicio(dado, lista)
        elif opc == 2:
            percorrer_lista(lista)
        elif opc == 3:
            dado = int(input("Digite um valor: "))
            lista = adicionar_final(dado, lista)
        elif opc == 4:
            media_valor(lista)
        elif opc == 5:
            ("Sair")
main()
