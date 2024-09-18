def iniciar():
    print(f'Tecle 1 para listar os alunos cadastrados.\n'
            f'Tecle 2 para cadastrar um aluno.\n'
            f'Tecle 3 para excluir um aluno.\n'
            f'Tecle 0 para encerrar o programa.')
    print('-'*50)


def mostrar_alunos(alunos):
    if not alunos:
        print('Ainda não há alunos cadastrados')
    else:
        for aluno in alunos:
            print(f'{aluno.nome} | Ano de Nascimento:{aluno.ano_nascimento} | Idade: {aluno.idade} anos')  

def capturar_dados_aluno():
    nome = input('Insira o nome do aluno: ')
    ano_nasc = int(input('Insira o ano de nascimento o aluno: '))
    return nome, ano_nasc

def aluno_para_excluir():
    return input('Insira o nome do aluno que deseja excluir: ')
