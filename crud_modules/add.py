from crud_modules import firebase_settings
database = firebase_settings.admin_db

def adicionar_novo_item(item):
    try:
        ref = database.reference("/itens")
        ref.push(item['titulo']).set(item)
        # database.child("itens").update({item['titulo']:item})
        return f"[!] O item {item['titulo']} foi adicionado com sucesso ao banco de dados.\n"
    
    except Exception as erro:
        return f"[X] Houve um erro ao adicionar o item ao banco de dados.\n--> {erro}\n"

def criar_novo_item():
    titulo = input("> Digite o título do item: ")
    descricao = input("> Digite a descrição: ")
    preco = float(input("> Qual o valor deste item? R$").replace(",", "."))
    lactose = input("> Contém lactose? (S/n): ").upper()

    yes = ['S', '']

    lactose = lactose in yes
    vegan = False

    if not lactose:
        vegan = input("> É vegano? (S/n): ").upper()
        vegan = vegan in yes
    
    opcoes = input("> Este item contém uma versão alternativa?\nEx.: Sem lactose, com chantilly, descafeinado...? (S/n): ").upper()
    opcoes = opcoes in yes

    alt_list = False
    if opcoes:
        alt_list = []
        alt_qtd = int(input("> Quantas alternativas tem? (número inteiro): "))
        
        while alt_qtd > 0:
            alt_qtd = alt_qtd - 1
            alt_name = input("\n> Qual o nome desta alternativa? (Ex.: Sem lactose): ")
            alt_cost = float(input("> Qual o valor adicional para esta alternativa? (0 para nulo): ").replace(",", "."))
            alt_list.append({
                "nome": alt_name,
                "preco": alt_cost
            })
    
    estoque = input("> O item já está em estoque e pronto para ser comercializado? (S/n): ")
    estoque = estoque in yes

    static_image_link = input("> Insira o link estático da imagem de destaque do item\n Caso CTRL + V não funcione, tente CTRL + SHIFT + V para colar: ")

    categoria = input(
        f"\n{'-'*26} Categorias {'-'*26}\n" +
        "(1) Lanches\n" +
        "(2) Cafés\n" +
        "(3) Doces\n" +
        "(4) Bebidas\n" +
        "\n[?] Em qual categoria o item pertence? "
    )

    item = {
        "titulo": titulo,
        "descricao": descricao,
        "preco": preco,
        "lactose": lactose,
        "vegan": vegan,
        "adicionais": alt_list,
        "estoque": estoque,
        "image_link": static_image_link,
        "categoria": categoria
    }
    # print(item['adicionais'][0])
    print(f"{'-'*10} Resumo do Item: {'-'*10}")
    
    for chave in item:
        print(f"🞄 {chave}: {item[chave]}")
    
    confirm = input(f"{'-'*26}\n> Está tudo correto? (S/n): ")
    confirm = confirm in yes

    if confirm:
        return item
    else:
        print("[x] Operação cancelada.\n")
        return False
