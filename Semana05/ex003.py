class No:
    def __init__(self, nome, idade, prioridade):
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade
        self.proximo = None
        self.anterior = None


def inserirPaciente(lista, nome, idade, prioridade):
    novo = No(nome, idade, prioridade)

    if lista is None:
        novo.proximo = novo
        novo.anterior = novo
        return novo

    lista.anterior.proximo = novo
    novo.anterior = lista.anterior
    novo.proximo = lista
    lista.anterior = novo

    return lista


def removerPaciente(lista, nome):
    if lista is None:
        return lista, False

    aux = lista

    while True:
        if aux.nome == nome:
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


def mostrarPacientes(lista):
    if lista is None:
        print("Nao ha pacientes na fila.")
        return

    aux = lista

    while True:
        print("Nome:", aux.nome, "| Idade:", aux.idade, "| Prioridade:", aux.prioridade)
        aux = aux.proximo

        if aux == lista:
            break


def buscarPacientePrioridade(lista, prioridade):
    if lista is None:
        return None

    aux = lista

    while True:
        if aux.prioridade == prioridade:
            return aux

        aux = aux.proximo

        if aux == lista:
            break

    return None


def simularAtendimento(lista):
    if lista is None:
        print("Nao ha pacientes para atendimento.")
        return lista

    while lista is not None:
        paciente = buscarPacientePrioridade(lista, "emergencia")

        if paciente is None:
            paciente = buscarPacientePrioridade(lista, "urgente")

        if paciente is None:
            paciente = buscarPacientePrioridade(lista, "normal")

        print("Paciente atendido:", paciente.nome, "| Idade:", paciente.idade, "| Prioridade:", paciente.prioridade)
        lista, removido = removerPaciente(lista, paciente.nome)

    print("Todos os pacientes foram atendidos.")
    return lista


def main():
    lista = None

    while True:
        print("\n--- MENU ---")
        print("1 - Inserir paciente")
        print("2 - Remover paciente atendido")
        print("3 - Mostrar todos os pacientes")
        print("4 - Simular atendimento")
        print("5 - Sair")

        op = int(input("Escolha uma opcao: "))

        if op == 1:
            nome = input("Digite o nome do paciente: ")
            idade = int(input("Digite a idade: "))
            prioridade = input("Digite a prioridade (emergencia, urgente, normal): ")
            lista = inserirPaciente(lista, nome, idade, prioridade)
            print("Paciente inserido com sucesso.")

        elif op == 2:
            nome = input("Digite o nome do paciente atendido: ")
            lista, removido = removerPaciente(lista, nome)

            if removido:
                print("Paciente removido com sucesso.")
            else:
                print("Paciente nao encontrado.")

        elif op == 3:
            mostrarPacientes(lista)

        elif op == 4:
            lista = simularAtendimento(lista)

        elif op == 5:
            print("Encerrando o programa.")
            break

        else:
            print("Opcao invalida.")


main()
