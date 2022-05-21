import json
import string

from typing import Dict
# 1 - Digitar o nome completo, telefone de contato e e-mail da pessoa
# 2 - Adicionar elementos a uma lista organizada
# 3 - Ler a lista item a item
# 4 - Adicionar os itens da lista aos contatos do google


def remove_punctuation(inputed_string: str) -> str:
    return inputed_string.translate(str.maketrans('', '', string.punctuation))


def adicionar_lista(nome: str,
                    telefone: str,
                    email: str) -> Dict[str, str]:

    dicionario = {
        "Nome": nome,
        "Telefone": remove_punctuation(telefone.replace(" ", "")),
        "Email": email
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
    while True:
        decidir = input('Para parar digite "0", para continuar, precione qualquer outra tecla.')
        if decidir == "0":
            break

        nome = input("Digite um nome para o contato: ")

        while not nome:
            nome = input("Digite um nome para o contato: ")

        telefone = input("Digite um telefone: ")

        while not telefone.isdigit():
            print("O valor digitado nao era um numero")
            telefone = input("Digite um telefone: ")

        while not telefone:
            telefone = input("Digite um telefone: ")

        email = input("Digite um email para o contato: ")

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
