import json
import pandas as pd
import os

# 1 - Digitar o nome completo, telefone de contato e e-mail da pessoa
# 2 - Adicionar elementos a uma lista organizada
# 3 - Ler a lista item a item
# 4 - Adicionar os itens da lista aos contatos do google


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
