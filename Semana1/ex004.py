class Livro:
    def __init__(self, titulo, autor, numerop):
        self.titulo = titulo
        self.autor = autor
        self.numerop = numerop
    
    def livro_curto_longo(self):
        print("Titulo: ", self.titulo)
        print("Autor: ", self.autor)
        if self.numerop <= 100:
            print("Livro curto")
        else:
            print("Livro longo")

Livro1 = Livro("AAA1", "Gustavo", 101)
Livro2 = Livro("AAA2", "Arthur", 99)

Livro1.livro_curto_longo()
Livro2.livro_curto_longo()