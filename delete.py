import firebase_settings
database = firebase_settings.database

def delete(item):
    try:
        database.child("itens").remove(item['titulo'])
        return f"[!] O item {item['titulo']} foi removido com sucesso.\n"
    
    except Exception as erro:
        return f"[X] Houve um erro ao remover o item ao banco de dados.\n--> {erro}\n"


def listar_todos_itens():
    print('-'*26 + ' Deletando Itens ' + '-'*26)
    all_itens = database.child('itens').get().val()
    for item in all_itens:
        print(f"• {item}")