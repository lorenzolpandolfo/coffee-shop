from flask import Blueprint, render_template, redirect, session, url_for, request, jsonify
from crud_modules import firebase_settings
import json

carrinho_bp = Blueprint("carrinho", __name__, template_folder="templates")


def somar_precos():
    carrinho = session["carrinho"]
    valorTotal = 0
    for item in carrinho:
        preco = item["preco"]
        valorTotal += preco
    
    return round(valorTotal,3)


@carrinho_bp.route("/carrinho", methods=["POST", "GET"])
def carrinho():
    if request.method == "GET":
        button_value = request.args.get('item')

        # Removendo item do carrinho
        if button_value:
            item = button_value.replace("'", '"').replace("True", "true").replace("False", "false")
            item = json.loads(item)

            # print(session["carrinho"])
            # print('removendo ', item)

            session["carrinho"].remove(item)
            session["carrinhoLocal"] = session["carrinho"]
            session.modified = True

            return jsonify({'quantidade_carrinho': len(session["carrinho"])})
            
    return render_template("carrinho.html",
                           USER=session,
                           ITENS_CARRINHO=session['carrinho'],
                           QUANTIDADE_CARRINHO=len(session["carrinho"]),
                           soma_precos = somar_precos())