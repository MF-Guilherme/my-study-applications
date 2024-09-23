from controllers import FuncionarioController
import views

def exibir_funcionarios():
    funcionarios = func_controller.listar_funcionarios()
    views.listar_funcionarios(funcionarios)

def cadastrar_funcionario():
    nome, cpf, ano_nasc, id_func, cargo, salario_base = views.dados_funcionario()
    func_controller.cadastrar_funcionario(nome, cpf, ano_nasc, id_func, cargo, salario_base)

def excluir_funcionario():
    id_funcionario = views.id_func_excluir()
    func_controller.excluir_funcionario(id_funcionario)

def exibir_salario():
    id_funcionario = views.exibir_salario_funcionario()
    func_controller.exibir_salario_funcionario(id_funcionario)

func_controller = FuncionarioController()

while True:

    views.mostrar_menu()

    menu = input()
    print('-' * 50)
    
    if menu == '0':
        print('Programa encerrado.')
        break
    elif menu == '1':
        exibir_funcionarios()
    elif menu == '2':
        cadastrar_funcionario()
    elif menu == '3':
        excluir_funcionario()
        exibir_funcionarios()
    elif menu == '4':
        exibir_salario()
    
    
    