from flask import Blueprint, render_template, redirect, session, url_for, request
import firebase_settings
import json

carrinho_bp = Blueprint("carrinho", __name__, template_folder="templates")


@carrinho_bp.route("/carrinho", methods=["POST", "GET"])
def carrinho():
    if request.method == "POST":
        botao = request.form['botao']

        item = request.form['item'].replace("'", '"').replace("True", "true").replace("False", "false")
        item = json.loads(item)


        if botao == "removerDoCarrinho":
            session["carrinho"].remove(item)
            session.modified = True
    
    return render_template("carrinho.html", ITENS_CARRINHO=session['carrinho'])