import firebase_settings
import read
database = firebase_settings.database

def delete(item):
    try:
        database.child("itens").child(item).remove()
        return f"[!] O item {item} foi removido com sucesso.\n"
    
    except Exception as erro:
        return f"[X] Houve um erro ao remover o item ao banco de dados.\n--> {erro}\n"


def selecionar_item():
    print('-'*26 + ' Deletando Itens ' + '-'*26)
    read.ler_todos_itens()
    escolha = input("> Digite o nome do item para ser excluído: ")
    return escolha