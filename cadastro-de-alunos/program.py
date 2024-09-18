from models import Pessoa

def iniciar():
    print(f'Tecle 1 para listar os alunos cadastrados.\n'
            f'Tecle 2 para cadastrar um aluno.\n'
            f'Tecle 3 para excluir um aluno.\n'
            f'Tecle 0 para encerrar o programa.')
    print('-'*50)

def listar_alunos(db):
    for aluno in db:
        print(f'{aluno.nome} | Ano de Nascimento:{aluno.ano_nascimento} | Idade: {aluno.idade} anos')

def cadastrar_aluno(db):
    nome = input('Insira o nome do aluno: ')
    ano_nasc = int(input('Insira o ano de nascimento do aluno: '))
    aluno = Pessoa(nome, ano_nasc)
    db.append(aluno)
    print('Aluno cadastrado com sucesso!')
    return db

def excluir_aluno(db):
    nome = input('Insira o nome do aluno que deseja excluir: ')
    aluno_encontrado = False
    for aluno in db:
        if aluno.nome == nome:
            db.remove(aluno)
            aluno_encontrado = True
            return 'Aluno excluído com sucesso!'
    if not aluno_encontrado:
        return 'Aluno não encontrado na lista.'

db = []

while True:
    iniciar()

    inp = input()

    if inp == '0':
        print('Programa encerrado')
        break

    elif inp == '1':
        if not db:
            print('Ainda não há alunos cadastrados')
        else:
            listar_alunos(db)
            
    elif inp == '2':        
        db = cadastrar_aluno(db)
        pass

    elif inp == '3':
        print(excluir_aluno(db))
        pass
    print('-'*50)



