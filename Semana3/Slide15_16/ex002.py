class No:
    def __init__(self, musicID, musicName, artist, musicDuration):
        self.musicID = musicID
        self.musicName = musicName
        self.artist = artist
        self.musicDuration = musicDuration
        self.proximo = None
        self.anterior = None



def addMusic(lista, musicID, musicName, artist, musicDuration):
    novo = No(musicID, musicName, artist, musicDuration)
    if lista == None:
        lista = novo
        return lista
    
    lista.anterior = novo
    novo.proximo = lista
    lista = novo
    return lista



def listMusic(lista):
    aux = lista

    if aux is None:
        print("Lista vazia!")
        return

    while aux is not None:
        print(f"ID da Música: ", aux.musicID)
        print(f"Nome da Música: ", aux.musicName)
        print(f"Artista: ", aux.artist)
        print(f"Duração da música: ", aux.musicDuration,"min")
        aux = aux.proximo



def removeMusic(lista, musicID, musicName):
    aux = lista
    if lista is None:
        print("Lista vazia!")
        return lista
    
    print("1 - Remover por ID")
    print("2 - Remover por nome da música")
    opc = int(input("Digite a opção: "))

    if opc == 1:
        idmusic = int(input("Digite o ID da música: "))
        while aux is not None:
            if aux.musicID == idmusic:
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
        print("Música não encontrada!")
        return lista

    elif opc == 2:
        namemusic = input("Digite o nome da música: ")
        while aux is not None:
            if aux.musicName == namemusic:
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
        print("Música não encontrada!")
        return lista
    else:
        print("Opção inválida!")
        return lista


def searchMusic(lista, musicName, artist):
    aux = lista
    if lista is None:
        print("Lista vazia!")
        return
    print("1 - Buscar por artista")
    print("2 - Buscar por nome da música")
    opc = int(input("Digite a opção: "))

    if opc == 1:
        artistname = input("Digite o nome do artista").upper()
        encontrou = False
        while aux is not None:
            if aux.artist.upper() == artistname:
                print("Música encontrada deste artista: ", aux.musicName)
                encontrou = True
            aux = aux.proximo
        if not encontrou:
            print("Músicas deste artista não encontradas!")
        
    elif opc == 2:
        namemusic = input("Digite o nome da música: ")
        encontrou = False
        while aux is not None:
            if aux.musicName == namemusic:
                print("Música encontrada: ", aux.musicName)
                encontrou = True
            aux = aux.proximo
        if not encontrou:
            print("Nenhuma música encontrada com este nome!")



def playlist_duration(lista, musicDuration):
    aux = lista
    total = 0
    while aux is not None:
        total += aux.musicDuration
        aux = aux.proximo
    print("Tempo total da playlist: ", total)
    return




def navigateMusic(lista):
    atual = lista
    if atual is None:
        print("Lista vaiza!")
        return
    
    print("Música atual: ", atual.musicName)
    print("1 - Próxima música")
    print("2 - Música anterior")
    opc = int(input("Digite a opção: "))
    if opc == 1:
        if atual.proximo == None:
            print("Última música!")
            return atual
        atual = atual.proximo
        print("Música atual: ", lista.musicName)
        return atual
    elif opc == 2:
        if atual.anterior == None:
            print("Primeira música!")
            return atual
        atual = atual.anterior
        print("Música atual: ", lista.musicName)
        return atual

        




def menu():
    print('''
1 - Adicionar música na playlist
2 - Listar todas as músicas
3 - Remover música
4 - Buscar música (por nome ou por artista)
5 - Mostrar a duração total da playlist
6 - Avançar para a próxima música / Voltar para a música anterior 
(usando os ponteiros da lista)
7 - Sair   ''')
    opc = int(input("Digite uma opção: "))
    return opc





def main():
    lista = None
    opc = 0

    while opc != 7:
        opc = menu()
        if opc == 1:
            musicID = int(input("Digite o ID da música: "))
            musicName = input("Digite o nome da música: ")
            artist = input("Digite o artista: ")
            musicDuration = float(input("Digite o tempo da música: "))
            lista = addMusic(lista, musicID, musicName, artist, musicDuration)
        elif opc == 2:
            listMusic(lista)
        elif opc == 3:
            lista = removeMusic(lista, musicID, musicName)
        elif opc == 4:
            searchMusic(lista, musicName, artist)
        elif opc == 5:
            playlist_duration(lista, musicDuration)
        elif opc == 6:
            lista = navigateMusic(lista)
        elif opc == 7:
            print("Saindo")
main()

