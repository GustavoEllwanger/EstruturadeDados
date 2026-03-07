class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    
    def calcular_bonus(self):
        if self.cargo == "Gerente".upper():
            self.salario *= 1.10
            print("Novo salário:", self.salario)
        else:
            self.salario *= 1.05
            print("Novo salário: ", self.salario)


Gerente = Funcionario("Claudio", 5000, "Gerente".upper())
Assistente = Funcionario("Ricardo", 1394, "Assistente")
Estagiario = Funcionario("Gustavo", 800, "Estagiário")

Gerente.calcular_bonus()
Assistente.calcular_bonus()
Estagiario.calcular_bonus()