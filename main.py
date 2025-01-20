from buyListManager import add_item, remove_item, show_list

def main():
    print('|---LISTA DE COMPRAS---|')
    print('|--[1] Adicionar item--|')
    print('|---[2] Remover item---|')
    print('|----[3] Ver lista-----|')
    print('|-------[4] Sair-------|')

    while True:
        try:
            option = int(input('Escolha uma opção: '))
        except ValueError:
            print('Opção inválida!')
            continue

        if option == 1:
            itemToBeAdded = input('Digite o item a ser adicionado: ')
            try:
                itemCode = int(input('Digite o código do item: '))
            except ValueError:
                print('Código inválido!')
            add_item(itemToBeAdded, itemCode)
        elif option == 2:
            itemCodeToBeRemoved = int(input('Digite o código do item a ser removido: '))
            remove_item(itemCodeToBeRemoved)
        elif option == 3:
            show_list()
        elif option == 4:
            print('Saindo...')
            break

if __name__ == '__main__':
    main()