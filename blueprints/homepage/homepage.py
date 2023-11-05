from flask import Blueprint, render_template, redirect, session, url_for, request, jsonify
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
            
        button_value = request.args.get('button_item_value')

        if request.method == "GET":

            # adicionar o item ao carrinho usando ajax jquery
            if button_value:
                item = button_value.replace("'", '"').replace("True", "true").replace("False", "false")
                item = json.loads(item)

                session["carrinho"].append(item)
                session.modified = True

                return jsonify({'quantidade_carrinho': len(session["carrinho"])})

        qtd_item_carrinho = len(session["carrinho"])
        return render_template("homepage.html", USER=session, ITENS_CARDAPIO=get_item_data(), QTD_ITEM_CARRINHO=qtd_item_carrinho)
    
    else:
        return render_template("homepage.html", USER=False, ITENS_CARDAPIO=get_item_data())
