from models import Aluno


class AlunoController:
    def __init__(self):
        self.db = []    
    
    def listar_alunos(self):
        return self.db

    def cadastrar_aluno(self, nome, ano_nasc):
        aluno = Aluno(nome, ano_nasc)
        self.db.append(aluno)
        return 'Aluno cadastrado com sucesso!'       

    def excluir_aluno(self, nome):
        aluno_encontrado = False
        for aluno in self.db:
            if aluno.nome == nome:
                self.db.remove(aluno)
                aluno_encontrado = True
                return 'Aluno excluído com sucesso!'
        if not aluno_encontrado:
            return 'Aluno não encontrado na lista.'