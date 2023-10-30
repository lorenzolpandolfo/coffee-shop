import firebase_settings
database = firebase_settings.database


def ler_todos_itens():
    all_itens = database.child('itens').get().val()
    
    for item in all_itens:
        print(f"• {item}")
    
    return 0