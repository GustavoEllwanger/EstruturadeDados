class Aluno:
    def __init__(self, nome, n1, n2, n3):
        self.nome = nome
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def calcular_media(self):
        self.media = (self.n1 + self.n2 + self.n3) / 3
        return self.media

Gustavo = Aluno("Gustavo", 8, 9, 7)
Arthur = Aluno("Arthur", 5, 7, 3)
Andrei = Aluno("Andrei", 7, 7, 8)

turma = []


turma.append(Gustavo)
turma.append(Arthur)
turma.append(Andrei)


for i in range(3):
    print(turma[i].nome)
    print(turma[i].calcular_media())
    
    
