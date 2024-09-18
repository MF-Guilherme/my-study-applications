class Empregado:
    def __init__(self, nome, cpf, idade, salario_base):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.salario_base = salario_base

    def salario_liquido(self):
        return self.salario_base * 0.90


class Gerente(Empregado):
    def __init__(self, nome, cpf, idade, salario_base):
        super().__init__(nome, cpf, idade, salario_base)
    
    def salario_liquido(self):
        return self.salario_base * 0.95


emp = Empregado('Guilherme', '2312432', 32, 1200)
ger = Gerente('Andressa', '5461131', 28, 4000)

print(emp.salario_liquido())
print(ger.salario_liquido())

