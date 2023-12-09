from crud_modules import firebase_settings, read
database = firebase_settings.admin_db

def delete(item):
    try:
        item_to_remove_id = read.ler_todos_itens(False, item)
        item_to_remove = database.reference(f"itens/{item_to_remove_id}").delete()
        return f"[!] O item foi removido com sucesso.\n"
    
    except Exception as erro:
        return f"[X] Houve um erro ao remover o item ao banco de dados.\n--> {erro}\n"


def selecionar_item():
    print('-'*26 + ' Deletando Itens ' + '-'*26)
    read.ler_todos_itens()
    escolha = int(input("> Digite o número do item para ser excluído: "))
    return escolha