def mostrar_menu():
    print(f'Tecle 1 para listar todos os funcionários\n'
          f'Tecle 2 para cadastrar um funcionário\n'
          f'Tecle 3 para excluir um funcionário\n'
          f'Tecle 0 para sair\n')
    print('-' * 50)

def listar_funcionarios(funcionarios):
    if not funcionarios:
        print('Ainda não há funcionários cadastrados')
    else:
        for funcionario in funcionarios:
            print(f'Código: {funcionario.id_func} | Nome: {funcionario.nome} | Cargo: {funcionario.cargo} | Salário: {funcionario.salario}')




