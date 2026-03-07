class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email



    def nomeadd(self):
        print("Nome: ", self.nome)


    def telefoneadd(self):
        print("Telefone: ", self.telefone)


    def emailadd(self):
        print("Email: ", self.email )

        
agenda = []

Gustavo = Contato("Gustavo", 555, "aaa@gmail.com")
Arthur = Contato("Arthur", 666, "bbb@gmail.com")
Andrei = Contato("Andrei", 777, "ccc@gmail.com")


agenda.append(Gustavo)
agenda.append(Arthur)
agenda.append(Andrei)
for i in range (3):
    print(agenda[i].nome)
    print(agenda[i].telefone)
    print(agenda[i].email)



