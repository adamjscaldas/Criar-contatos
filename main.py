import pandas as pd
import os
from typing import Dict
import json


def clean_number(number_to_clean: str) -> str:
    items_removed = """ ,.+-=()_;:|\\/´`~^[]{}*&¨%$#@!?'"><
    AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzÇç"""
    cleaned_number = number_to_clean
    for x in range(len(items_removed)):
        cleaned_number = cleaned_number.replace(items_removed[x], '')
    return cleaned_number


def clean_name(name_to_clean: str) -> str:
    items_removed = """0123456789-_=+()[]{}:?<>,.;/\\|'"!@#$%¨&*"""
    cleaned_name = name_to_clean
    for x in range(len(items_removed)):
        cleaned_name = cleaned_name.replace(items_removed[x], '')
    return cleaned_name


def create_list(dataframe: pd.core.frame.DataFrame, contador1: int) -> list:
    list_returned = []
    for contador2 in range(len(df.index)):
        data1 = dataframe.iat[contador1, contador2]
        print(f'O elemento "{data1}" na posição (0, {contador2}) do tipo: {type(data1)}')
        data1 = str(data1)
        if data1 == 'nan':
            data1 = None
            list_returned.append(data1)
        else:
            list_returned.append(data1)
    try:
        list_returned.remove(None)
    except ValueError:
        pass
    finally:
        pass
    return list_returned


def create_dict(name: str,
                phonenumber: str,
                email: str) -> Dict[str, str]:
    dicionario = {
        "Nome": name,
        "Telefone": phonenumber,
        "Email": email.replace(' ', '')
    }
    return dicionario



def save_json(dicionario: Dict[str, str]) -> None:
    with open("contatos.json", "r+") as json_file:
        lines = json_file.read()
        if not lines:
            json_file.write("[]")

    with open("contatos.json", 'r+') as json_file:
        data = json.load(json_file)
        data.append(dicionario)

    with open("contatos.json", 'w') as json_file:
        json.dump(data, json_file, indent=4, separators=(',', ': '))

    print("Tudo certo, seu arquivo foi escrito")


if __name__ == '__main__':
    abspath = os.path.abspath(__file__)
    loc = os.path.dirname(abspath) + "\\Lista Contatos Teste.xlsx"
    df = pd.read_excel(io=loc, sheet_name=0)
    dicionario = {}

    for contador1 in range(len(df.index)):
        lista = create_list(dataframe=df, contador1=contador1)
        print(lista)
        dicionario = create_dict(name=lista[0], phonenumber=lista[1], email=lista[2])
        # save_json(dicionario=dicionario)
    print(dicionario)
