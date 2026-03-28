class No:
    def __init__(self, id):
        self.id = id
        self.proximo = None
        self.anterior = None
    



def addAtleta(lista, id):
        novo = No(id)
        if lista is None:
            novo.proximo = novo
            novo.anterior = novo
            lista = novo
            return lista
        
        lista.anterior.proximo = novo
        novo.anterior = lista.anterior
        lista.anterior = novo
        novo.proximo = lista
        lista = novo
        return lista




def removerAtleta(lista, id):
     aux = lista
     while True:
            if aux.id == id:
                if aux == aux.proximo == aux.anterior:
                    return None
                aux.anterior.proximo = aux.proximo
                aux.proximo.anterior = aux.anterior
                if aux == lista:
                     lista = lista.proximo
                     return lista
            aux = aux.proximo

            if aux == lista:
                 print("Elemento não encontrado")
                 return lista


def passarBastao(lista):
    aux = lista
    lista.bastao = True

    for i in range(10):
         print("Atleta com o bastão: ", aux.id)
         
         aux.bastao = False
         aux = aux.proximo
         aux.bastao = True





def menu():
     print("1 - Adicionar atleta")
     print("2 - Remover atleta")
     print("3 - Passar bastão")
     print("4 - Sair")
     opc = int(input("Digite uma opção: "))
     return opc




def main():
     lista = None
     opc = 0

     while opc != 4:
          opc = menu()

          if opc == 1:
               id = input("Digite o nome do atleta: ")
               lista = addAtleta(lista, id)
          elif opc == 2:
               id = input("Digite o nome do atleta: ")
               lista = removerAtleta(lista, id)
          elif opc == 3:
               passarBastao(lista)
               
main()
