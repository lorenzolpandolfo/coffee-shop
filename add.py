def adicionar_novo_item():
    titulo = input("> Digite o título do item: ")
    descricao = input("> Digite a descrição: ")
    lactose = input("> Contém lactose? (S/n): ").upper()
    lactose = lactose in ['S', '']
    vegan = False

    if lactose:
        vegan = False
    else:
        vegan = input("> É vegano? (S/n): ").upper()
        vegan = vegan in ['S', '']

    print(f"Resultados:\nvegan: {vegan}\nlactose:{lactose}")

    """
    if lactose == 'S' or lactose == '':
        lactose = True

    else:
        lactose = False
        vegan = input("> É vegano? (S/n): ").upper()
        if vegan == 'S' or vegan == '':
            vegan = True
        else:
            vegan = False
    """