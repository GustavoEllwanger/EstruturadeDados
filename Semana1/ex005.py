class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    
    def calcular_bonus(self):
        if self.cargo == "Gerente":
            return self.salario * 1.10
        else:
            return self.salario * 1.05


Gerente = Funcionario("Claudio", 5000, "Gerente")
Assistente = Funcionario("Ricardo", 1394, "Assistente")
Estagiario = Funcionario("Gustavo", 800, "Estagiário")

print(Gerente.nome, "Salário com bônus: ", Gerente.calcular_bonus())
print(Assistente.nome, "Salário com bônus: ", Assistente.calcular_bonus())
print(Estagiario.nome, "Salário com bônus: ", Estagiario.calcular_bonus())
