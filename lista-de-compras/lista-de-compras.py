def inserir_itens(lista):
    itens = ""
    print('Insira o produto e tecle Enter, para finalizar digite 0 (zero)')
    while True:
        item = input()
        if item == '0':
            break
        lista.append(item)
    return lista

def remover_item(item, lista):
    if item in lista:
        lista.remove(item)
        print(f'{item} removido da sua lista de compras')

def exibir_lista(lista):
    if lista:
        for item in lista:
            print(item)
    else:
        print('Ainda não há nenhum produto na sua lista')
        

lista = []

while True:
    print(f'Tecle 1 para visualizar a lista.\n'
        f'Tecle 2 para inserir produtos na lista.\n'
        f'Tecle 3 para excluir um produto da lista.\n'
        f'Tecle 0 para encerrar o programa.')
    inp = input()
    if inp == '0':
        print('Programa encerrado')
        break
    elif inp == '1':
        exibir_lista(lista)
    elif inp == '2':
        lista = inserir_itens(lista)
    elif inp == '3':
        produto = input('Insira o nome do produto que deseja excluir: ')
        if not produto in lista:
            print('Esse produto não está na lista, verifique o nome e tente novamente')
        else:
            remover_item(produto, lista)
    else:
        print('Insira apenas um número válido')
        pass
