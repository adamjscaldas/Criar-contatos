import json

import keyboard
from keyboard import is_pressed

# 1 - Digitar o nome completo, telefone de contato e e-mail da pessoa
# 2 - Adicionar elementos a uma lista organizada
# 3 - Ler a lista item a item
# 4 - Adicionar os itens da lista aos contatos do google


def testar(variavel):
    if variavel == '':
        return 0
    else:
        return 1


def repetir(variavel):
    valor = input(f'{variavel}: ')
    while testar(valor) == 0:
        repetir(variavel)
    return valor


def adicionarlista():
    nome = repetir("Nome")
    telefone = repetir("Telefone")
    email = repetir('E-mail')
    dicionario = {
        'nome': f'{nome}',
        'telefone': f'{telefone}',
        'email': f'{email}'
    }
    return dicionario


def salvar_json(arquivo, dicionario):
    with open(arquivo, 'r+') as json_file:
        data = json.load(json_file)
        data.append(dicionario)
    with open(arquivo, 'w') as json_file:
        json.dump(data, json_file, indent=4, separators=(',', ': '))


def loop():
    while True:
        decidir = input('Para parar digite "0", para continuar, precione qualquer outra tecla. ')
        if decidir == "0":
            break
        dicionario_add = adicionarlista()
        salvar_json('contatos.json', dicionario_add)


loop()
