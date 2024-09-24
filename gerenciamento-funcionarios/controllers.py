from models import Funcionario, Gerente

class FuncionarioController():
    def __init__(self):
        self.db = []

    def listar_funcionarios(self):
        return self.db

    def cadastrar_funcionario(self, nome, cpf, ano_nasc, id_func, cargo, salario_base):
        if cargo == 'Gerente' or cargo == 'gerente':
            ger = Gerente(nome, cpf, ano_nasc, id_func, cargo, salario_base )
            self.db.append(ger)
            print('Funcionário cadastrado com sucesso!')
            print('-' * 50)
        else:
            func = Funcionario(nome, cpf, ano_nasc, id_func, cargo, salario_base)
            self.db.append(func)
            print('Funcionário cadastrado com sucesso!')
            print('-' * 50)
    
    def excluir_funcionario(self, id_func):
        id_encontrado = False
        if self.db:
            for func in self.db:
                if func.id_func == id_func:
                    self.db.remove(func)
                    id_encontrado = True
                    print('Funcionário excluído com sucesso!')
                    print('-' * 50)
            if not id_encontrado:
                print('Id de funcionário não encontrado')
                print('-' * 50)
        else: 
            print('Ainda não há nenhum funcionário cadastrado')
            print('-' * 50)

    def exibir_salario_funcionario(self, id_func):
        id_encontrado = False
        for funcionario in self.db:
            if funcionario.id_func == id_func:
                id_encontrado = True
                print(f'Código: {funcionario.id_func} | Nome: {funcionario.nome} | Cargo: {funcionario.cargo} | '
                    f'Salário Base: R${float(funcionario.salario_base):.2f} | '
                    f'Salário Líquido: R${float(funcionario.salario_liquido()):.2f}')
                print('-' * 50)                
        if not id_encontrado:
            print('Código funcional não encontrado')
            print('-' * 50)


    def retornar_funcionario(self, id_func):
        for funcionario in self.db:
            if funcionario.id_func == id_func:
                return funcionario
        
    def editar_funcionario(self, novo_nome, novo_cpf, novo_ano_nasc, id_func, novo_cargo, novo_salario_base):
        for funcionario in self.db:
            if funcionario.id_func == id_func:
                funcionario.nome = novo_nome
                funcionario.cpf = novo_cpf
                funcionario.ano_nasc = novo_ano_nasc
                funcionario.cargo = novo_cargo
                funcionario.salario_base = novo_salario_base
                return 'Dados alterados com sucesso'                
            else:
                return 'Funcionário não encontrado'
        print('-' * 50)
 
