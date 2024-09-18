from datetime import datetime, timezone

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento

    @property
    def idade(self):
        return datetime.now(timezone.utc).year - self.ano_nascimento

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
        return self.nome
    
    def alterar_ano_nasc(self, novo_ano_nasc):
        self.ano_nascimento = novo_ano_nasc
        return self.ano_nascimento




