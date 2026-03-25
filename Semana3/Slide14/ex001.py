class No:
    def __init__(self, id, nome, nota):
        self.id = id
        self.nome = nome
        self.nota = nota
        self.proximo = None
        self.anterior = None
    

def inserirAluno(id, nome, nota, lista):
    novo = No(id, nome, nota)
    if lista == None:
        lista = novo
        return lista
    
    lista.anterior = novo
    novo.proximo = lista
    lista = novo
    return lista



def listarAluno(lista):
    aux = lista
    if aux is None:
        print("Lista vazia")
        return
    while aux is not None:
        print("Alunos: ", aux.nome)
        print("ID: ", aux.id)
        aux = aux.proximo



def removerAluno(id, nome, lista):
    aux = lista
    while aux is not None:
        if aux.id == id and aux.nome == nome:
            if aux.proximo == aux.anterior == None:
                return None
            elif aux.anterior == None:
                lista = aux.proximo
                lista.anterior = None
                return lista
            elif aux.proximo == None:
                lista = aux.anterior
                lista.proximo = None
                return lista
            else:
                aux.anterior.proximo = aux.proximo
                aux.proximo.anterior = aux.anterior
                return lista
        aux = aux.proximo
    print("Aluno não encontrado")
    return



def mostrarSituacao(lista):
    aux = lista
    situacao = None
    if aux == None:
        print("Lista vazia")
        return
    while aux is not None:
        if aux.nota > 7:
            situacao = "Aprovado"
        elif aux.nota > 4:
            situacao = "Em exame"
        else:
            situacao = "Reprovado"
        print("Nome: ", aux.nome)
        print("Situação: ", situacao)
        aux = aux.proximo





def menu():
    print("1 - Inserir aluno")
    print("2 - Listar alunos")
    print("3 - Remover aluno")
    print("4 - Mostrar situação dos alunos")
    print("5 - Listar todos os alunos Aprovados, em exame e reprovados")
    opc = int(input("Digite a opção: "))
    return opc



def main():
    lista = None
    opc = 0
    while opc != 5:
        opc = menu()
        if opc == 1:
            nome = input("Digite o nome do aluno a inserir: ")
            id = int(input("Digite o ID do aluno: "))
            nota = float(input("Digite a nota final do aluno: "))
            lista = inserirAluno(id, nome, nota, lista)
        elif opc == 2:
            listarAluno(lista)
        elif opc == 3:
            nome = input("Digite o nome do aluno a remover: ")
            id = int(input("Digite o ID do aluno a remover: "))
            lista = removerAluno(id, nome, lista)
        elif opc == 4:
            mostrarSituacao(lista)

        

main()


    
