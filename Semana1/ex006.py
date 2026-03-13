class Aluno:
    def __init__(self, nome, n1, n2, n3):
        self.nome = nome
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.media = 0

    
    def calcular_media(self):
        self.media = (self.n1 + self.n2 + self.n3) / 3
        return self.media

    def verificar_aprovacao(self):
        if self.media >= 7:
            return "Aprovado"
        else:
            return "Reprovado"


Gustavo = Aluno("Gustavo", 8, 9, 7)
Arthur = Aluno("Arthur", 5, 7, 3)


print(Gustavo.nome, "- Média:", Gustavo.calcular_media(), "-", Gustavo.verificar_aprovacao())
print(Arthur.nome, "- Média:", Arthur.calcular_media(), "-", Arthur.verificar_aprovacao())

