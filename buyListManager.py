import json
import os

buyList = []
filePath = './GerenciadorDeCompras/buyList.json'

def add_item(item, itemCode):
    try:
        if os.path.exists(filePath):
            # Load existing data
            with open(filePath, "r", encoding="utf-8") as f:
                buyList = json.load(f)
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

    try:
        if os.path.exists(filePath):
            # Load existing data
            with open(filePath, "r", encoding="utf-8") as f:
                buyList = json.load(f)
    except FileNotFoundError:
        buyList = []
    except json.JSONDecodeError:
        buyList = []
    
    updated_buyList = [item for item in buyList if item['itemCode'] != itemCodeInput]

    if len(updated_buyList) == len(buyList):
        print('Item com o código especificado não foi encontrado.')
        return

    # Salvar a lista atualizada de volta no arquivo JSON
    with open(filePath, 'w') as file:
        json.dump(updated_buyList, file, indent=2)

def show_list():
    try:
        if os.path.exists(filePath):
            # Load existing data
            with open(filePath, "r", encoding="utf-8") as f:
                buyList = json.load(f)
    except FileNotFoundError:
        buyList = []
    except json.JSONDecodeError:
        buyList = []

    print('Lista de compras:')
    for item in buyList:
        print(f'{item["itemCode"]} | {item["item"]}')