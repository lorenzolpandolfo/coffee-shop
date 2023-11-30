import firebase_settings
database = firebase_settings.database

def adicionar_nova_loja(loja):
    try:
        database.child("stores").update({loja['id']:loja})
        return f"[!] A loja da rua {loja['rua']} foi adicionada com sucesso ao banco de dados.\n"
    
    except Exception as erro:
        return f"[X] Houve um erro ao adicionar a loja ao banco de dados.\n--> {erro}\n"

def criar_nova_loja():
    rua = input("> Digite o nome da rua da loja: ")
    numero = input("> Digite o número da loja: ")
    bairro = input("> Digite o bairro da loja: ")

    stores_db = database.child("stores").get().val()
    try:
        id = len(stores_db)

        while str(id) in stores_db:
            id += 1
    
    except Exception:
        id = 0

    loja = {
        "rua": rua,
        "numero": numero,
        "bairro": bairro,
        "id": id
    }

    print(f"{'-'*10} Resumo da Loja: {'-'*10}")
    
    for chave in loja:
        print(f"🞄 {chave}: {loja[chave]}")
    
    confirm = input(f"{'-'*26}\n> Está tudo correto? (S/n): ")

    yes = ['S', '']

    confirm = confirm in yes

    if confirm:
        return loja
    else:
        print("[x] Operação cancelada.\n")
        return False
