from crud_modules import firebase_settings
database = firebase_settings.admin_db


def ler_todos_itens(read=True, uid_get_by_title=None):
    all_itens = database.reference("itens")
    all_itens = all_itens.get()

    uuids = []
    
    for i, itemId in enumerate(all_itens):
        uuids.append(itemId)
        
        item = all_itens[itemId]
        
        if read:
            print(f"{i} - {item['titulo']}")

    # se eu quiser saber o uid de um item com titulo especifico
    if uid_get_by_title is not None:            
        return uuids[uid_get_by_title]
        
    
    else:
        return all_itens