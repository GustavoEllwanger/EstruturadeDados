class No:
    def __init__(self, parada):
        self.parada = parada
        self.proximo = None
        self.anterior = None



def adicionarParada(lista, parada):
    novo = No(parada)
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






def removerParada(lista, parada):
    if lista is None:
         print("Lista vazia!")
         return
    aux = lista
    while True:
            if aux.parada == parada:
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



def simularPercurso(lista):
     if lista is None:
          print("Lista vazia!")
          return
     aux = lista

     while True:
          print(aux.parada)
          aux = aux.proximo
          if aux == lista:
               return
          



def menu():
     print("1 - Adicionar parada")
     print("2 - Remover parada")
     print("3 - Simular percurso")
     print("4 - Sair")
     opc = int(input("Digite a opção:"))
     return opc



def main():
     lista = None
     opc = 0

     while opc != 4:
          opc = menu()
          if opc == 1:
               parada = input("Digite a parada para adicionar: ")
               lista = adicionarParada(lista, parada)
          elif opc == 2:
               parada = input("Digite a parada para remover: ")
               lista = removerParada(lista, parada)
          elif opc == 3:
               simularPercurso(lista)
          elif opc == 4:
               print("Saindo...")
          else:
               print("Opção inválida!")
main()
