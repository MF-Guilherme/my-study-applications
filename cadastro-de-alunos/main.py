from controllers import AlunoController
import views

controller = AlunoController()

while True:
    views.iniciar()

    inp = input()

    if inp == '0':
        print('Programa encerrado')
        break

    elif inp == '1':
        alunos = controller.listar_alunos()
        views.mostrar_alunos(alunos)
            
    elif inp == '2':
        nome, ano_nasc = views.capturar_dados_aluno()        
        print(controller.cadastrar_aluno(nome, ano_nasc))

    elif inp == '3':
        nome = views.aluno_para_excluir()
        print(controller.excluir_aluno(nome))

    print('-'*50)



