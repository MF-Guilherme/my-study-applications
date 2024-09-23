from prompt_toolkit import prompt

def mostrar_menu():
    print(f'Tecle 1 para listar todos os funcionários\n'
          f'Tecle 2 para cadastrar um funcionário\n'
          f'Tecle 3 para excluir um funcionário\n'
          f'Tecle 4 para editar um funcionário\n'
          f'Tecle 5 para exibir o salário de um funcionário\n'
          f'Tecle 0 para sair')
    print('-' * 50)

def listar_funcionarios(funcionarios):
    if not funcionarios:
        print('Ainda não há funcionários cadastrados')
    else:
        for funcionario in funcionarios:
            print(f'Código: {funcionario.id_func} | Nome: {funcionario.nome} | Cargo: {funcionario.cargo}')
    print('-'*50)

def dados_funcionario():
    nome = input('Digite o nome: ')
    cpf = input('Digite o cpf: ')
    ano_nasc = input('Digite o ano de nascimento: ')
    id_func = input('Digite o código funcional: ')
    cargo = input('Digite o cargo: ')
    salario_base = input('Digite o salário base: ')
    print('-' * 50)

    return nome, cpf, ano_nasc, id_func, cargo, salario_base

def id_func_excluir(funcionarios):
    if not funcionarios:
        print('Ainda não há funcionários cadastrados')
        print('-' * 50)
        return None
    else:
        id_func = input('Digite o id do funcionário que deseja excluir: ')
        print('-' * 50)
        return id_func

def exibir_salario_funcionario():
    id_funcionario = input('Digite o id do funcionário que deseja verificar o salário: ')
    print('-' * 50)
    return id_funcionario

def id_editar_funcionario(funcionarios):
    if not funcionarios:
        print('Ainda não há funcionários cadastrados')
        print('-' * 50)
        return None
    else:
        id_funcionario = input('Digite o id do funcionário que deseja editar: ')
        print('-' * 50)
        return id_funcionario

def dados_editar_funcionario(funcionario):
    novo_nome = prompt('Digite o nome: ', default=funcionario.nome)
    novo_cpf = prompt('Digite o cpf: ', default=funcionario.cpf)
    novo_ano_nasc = prompt('Digite o ano de nascimento: ', default=funcionario.ano_nasc)
    novo_id_func = funcionario.id_func
    novo_cargo = prompt('Digite o cargo: ', default=funcionario.cargo)
    novo_salario_base = prompt('Digite o salário base: ', default=funcionario.salario_base)
    print('-' * 50)
    return novo_nome, novo_cpf, novo_ano_nasc, novo_id_func, novo_cargo, novo_salario_base

        
