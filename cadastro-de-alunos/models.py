from datetime import datetime, timezone

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento

    @property
    def idade(self):
        return datetime.now(timezone.utc).year - self.ano_nascimento


class Aluno(Pessoa):
    def __init__(self, nome, ano_nascimento):
        super().__init__(nome, ano_nascimento)



