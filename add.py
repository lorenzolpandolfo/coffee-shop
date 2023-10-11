def adicionar_novo_item():
    titulo = input("> Digite o título do item: ")
    descricao = input("> Digite a descrição: ")
    lactose = input("> Contém lactose? (S/n): ").upper()

    yes = ['S', '']

    lactose = lactose in yes
    vegan = False

    if lactose:
        vegan = False
        opcoes = input("> Este item contém uma versão alternativa?\nEx.: Sem lactose, com chantilly, descafeinado...? (S/n): ").upper()
        opcoes = opcoes in yes
    else:
        vegan = input("> É vegano? (S/n): ").upper()
        vegan = vegan in yes
    
    link = input("> Insira o link estático da imagem de destaque do item (CTRL + SHIFT + V para colar): ")
    

