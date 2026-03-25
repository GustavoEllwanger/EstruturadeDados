class No:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.proximo = None
        self.anterior = None




def inserirNo(id, nome, lista):
    aux = lista
    while aux is not None:
        if aux.id == id:
            print("Id já existe!")
            return lista
        elif aux.nome == nome:
            print("Usuário já existe!")
            return lista
        aux = aux.proximo   

    novo = No(id, nome)

    if lista == None:
        lista = novo
        return lista
    
    lista.anterior = novo
    novo.proximo = lista
    lista = novo
    return lista

def listarNo(lista):
    aux = lista
    if aux is None:
        print("Lista vazia")
        return
    
    while aux is not None:
        print("Nome: ", aux.nome)
        print("ID: ", aux.id)
        aux = aux.proximo


def removerNo(lista):
    aux = lista
    if aux is None:
        print("Lista vazia")
        return lista
    print("1 - Remover por nome\n","2 - Remover por ID")
    opc = int(input("Digite a opção: "))
    if opc == 1:
        nome = input("Digite o nome: ")
        while aux is not None:
            if aux.nome == nome:
                if aux.proximo == aux.anterior == None:
                    return None
                elif aux.anterior == None:
                    lista = aux.proximo
                    lista.anterior = None
                    return lista
                elif aux.proximo == None:
                    aux.anterior.proximo = None
                    return lista
                else:
                    aux.anterior.proximo = aux.proximo
                    aux.proximo.anterior = aux.anterior
                    return lista
            aux = aux.proximo
    elif opc == 2:
        id = int(input("Digite o ID: "))
        while aux is not None:
            if aux.id == id:
                if aux.proximo == aux.anterior == None:
                    return None
                elif aux.anterior == None:
                    lista = aux.proximo
                    lista.anterior = None
                    return lista
                elif aux.proximo == None:
                    aux.anterior.proximo = None
                    return lista
                else:
                    aux.anterior.proximo = aux.proximo
                    aux.proximo.anterior = aux.anterior
                    return lista
            aux = aux.proximo
    print("Aluno não encontrado")
    return lista



def verificarNo(lista):
    aux = lista

    if aux is None:
        print("Lista vazia!")
        return

    print("1 - Verificar por nome\n", "2 - Verificar por ID")
    opc = int(input("Digite a opção: "))
    if opc == 1:
        nome = input("Digite o nome: ")
        while aux is not None:
            if aux.nome == nome:
                print(f"Nó com o nome: {nome} existe!")
                return
            aux = aux.proximo
        print(f"Nó com o nome: {nome} não existe!")
        return
    elif opc == 2:
        id = int(input("Digite o ID: "))
        while aux is not None:
            if aux.id == id:
                print(f"ID {id} existe!")
                return
            aux = aux.proximo
        print(f"Nó com o ID: {id} não existe!")
        return
        











def menu():
    print("1 - Inserir No")
    print("2 - Listar No's")
    print("3 - Remover No's")
    print("4 - Vertificar se No existe")
    print("5 - Sair")
    opc = int(input("Digite uma opção: "))
    return opc



def main():
    lista = None
    opc = 0

    while opc != 5:
        opc = menu()
        if opc == 1:
            nome = input("Digite o nome: ")
            id = int(input("Digite o ID: "))
            lista = inserirNo(id, nome, lista)
        elif opc == 2:
            listarNo(lista)
        elif opc == 3:
            lista = removerNo(lista)
        elif opc == 4:
            verificarNo(lista)
        elif opc == 5:
            print("Saindo...")
main()
