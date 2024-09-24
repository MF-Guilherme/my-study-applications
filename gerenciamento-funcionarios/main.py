from controllers import FuncionarioController
import views

def exibir_funcionarios():
    funcionarios = func_controller.listar_funcionarios()
    views.listar_funcionarios(funcionarios)

def cadastrar_funcionario():
    nome, cpf, ano_nasc, id_func, cargo, salario_base = views.dados_funcionario()
    func_controller.cadastrar_funcionario(nome, cpf, ano_nasc, id_func, cargo, salario_base)

def excluir_funcionario():
    funcionarios = func_controller.listar_funcionarios()
    id_funcionario = views.id_func_excluir(funcionarios)
    if not id_funcionario:
        pass
    else:
        func_controller.excluir_funcionario(id_funcionario)

def editar_funcionario():
    funcionarios = func_controller.listar_funcionarios()
    id_funcionario = views.id_editar_funcionario(funcionarios)
    if not id_funcionario:
        pass
    else:
        funcionario = func_controller.retornar_funcionario(id_funcionario)
        nome, cpf, ano_nasc, id_func, cargo, salario_base = views.dados_editar_funcionario(funcionario)
        print(func_controller.editar_funcionario(nome, cpf, ano_nasc, id_func, cargo, salario_base))
        print('-' * 50)

def exibir_salario():
    id_funcionario = views.exibir_salario_funcionario()
    func_controller.exibir_salario_funcionario(id_funcionario)

def editar_salario():
    views.editar_funcionario()

func_controller = FuncionarioController()

opcoes = {
    '1': exibir_funcionarios,
    '2': cadastrar_funcionario,
    '3': excluir_funcionario,
    '4': editar_funcionario,
    '5': exibir_salario
}

while True:
    views.mostrar_menu()
    menu = input()
    print('-' * 50)

    if menu == '0':
        print('Programa encerrado.')
        break
    elif menu in opcoes:
        opcoes[menu]()
    else:
        print('Opção inválida')