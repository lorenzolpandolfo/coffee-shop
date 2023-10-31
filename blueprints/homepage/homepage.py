from flask import Blueprint, render_template, redirect, session, url_for, request
import firebase_settings
import json

homepage_bp = Blueprint("homepage", __name__, template_folder="templates")

# Carregando os cafés para aparecerem na homepage
def get_item_data():
    database = firebase_settings.database
    # print(database.child('itens').get().val()['Capuccino'])
    return database.child('itens').get().val()


@homepage_bp.route("/", methods=['POST', 'GET'])
def home():
    # print(f"Session recebido no home: {session}")
    if session:
        # inicializando o carrinho
        if "carrinho" not in session:
            session["carrinho"] = []

        if request.method == 'POST':
            botao = request.form['botao']
            item = request.form['item']

            # para converter a string para o dicionario, precisa dessas correções abaixo
            item = request.form['item'].replace("'", '"').replace("True", "true").replace("False", "false")
            item = json.loads(item)

            if botao == "adicionarAoCarrinho":
                session["carrinho"].append(item)
                session.modified = True
        
        else:
            pass

        qtd_item_carrinho = len(session["carrinho"])
        return render_template("homepage.html", USER=session, ITENS_CARDAPIO=get_item_data(), QTD_ITEM_CARRINHO=qtd_item_carrinho)
    else:
        return render_template("homepage.html", USER=False, ITENS_CARDAPIO=get_item_data())
