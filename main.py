import json
import string

from typing import Dict


# 1 - Digitar o nome completo, telefone de contato e e-mail da pessoa
# 2 - Adicionar elementos a uma lista organizada
# 3 - Ler a lista item a item
# 4 - Adicionar os itens da lista aos contatos do google


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


def adicionar_lista(nome: str,
                    telefone: str,
                    email: str) -> Dict[str, str]:
    dicionario = {
        "Nome": clean_name(nome),
        "Telefone": clean_number(telefone),
        "Email": email.replace(' ', '')
    }

    return dicionario


def salvar_json(dicionario: Dict[str, str]) -> None:
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


def loop():
    nome = None
    telefone = None
    email = None
    while True:
        decidir = input('Para parar digite "0", para continuar, precione qualquer outra tecla.')
        if decidir == "0":
            break

        while not nome:
            nome = input("Digite um nome para o contato: ")
            nome = clean_name(nome)

        while not telefone:
            telefone = input("Digite um telefone: ")
            telefone = clean_number(telefone)

        while not email:
            email = input("Digite um email para o contato: ")

        dicionario_add = adicionar_lista(
            nome=nome,
            email=email,
            telefone=telefone
        )

        salvar_json(dicionario_add)


if __name__ == '__main__':
    loop()
