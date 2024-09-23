from datetime import datetime, timezone

class Pessoa:
    def __init__(self, nome, cpf, ano_nasc):
        self.nome = nome
        self.cpf = cpf
        self.ano_nasc = ano_nasc
    
    @property
    def idade(self):
        return datetime.now(timezone.utc).year - self.ano_nasc


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, ano_nasc, id_func, cargo, salario_base):
        super().__init__(nome, cpf, ano_nasc)
        self.id_func = id_func
        self.salario_base = salario_base
        self.cargo = cargo

    def salario_liquido(self):
        return self.salario_base * 0.90


class Gerente(Funcionario):
    def __init__(self, nome, cpf, ano_nasc, id_func, cargo, salario_base):
        super().__init__(nome, cpf, ano_nasc, id_func, cargo, salario_base)
    
    def salario_liquido(self):
        return self.salario_base * 0.95
