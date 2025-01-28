import json
buyList = []

def add_item(item, itemCode):
    filePath = 'buyList.json'

    try:
        with open(filePath, 'r') as file:
            buyList = json.load(file)
    except FileNotFoundError:
        buyList = []
    except json.JSONDecodeError:
        buyList = []

    itemToBeAdded = {"item": item, "itemCode": itemCode}
    buyList.append(itemToBeAdded)

    with open(filePath, 'w') as file:
        json.dump(buyList, file, indent=4)

def remove_item(itemCodeInput):
    global buyList

    file_path = 'buyList.json'

    try:
        with open(file_path, 'r') as file:
            buyList = json.load(file)
    except FileNotFoundError:
        buyList = []
    except json.JSONDecodeError:
        buyList = []
    
    updated_buyList = [item for item in buyList if item['itemCode'] != itemCodeInput]

    if len(updated_buyList) == len(buyList):
        print('Item com o código especificado não foi encontrado.')
        return

    # Salvar a lista atualizada de volta no arquivo JSON
    with open(file_path, 'w') as file:
        json.dump(updated_buyList, file, indent=2)

def show_list():

    file_path = 'buyList.json'

    try:
        with open(file_path, 'r') as file:
            buyList = json.load(file)
    except FileNotFoundError:
        buyList = []
    except json.JSONDecodeError:
        buyList = []

    print('Lista de compras:')
    for item in buyList:
        print(f'{item["itemCode"]} | {item["item"]}')