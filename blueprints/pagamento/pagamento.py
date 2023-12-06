from flask import Blueprint, render_template, redirect, session, url_for, request, jsonify
from crud_modules import firebase_settings
import json

pagamento_bp = Blueprint("pagamento", __name__, template_folder="templates")

def somar_preco_itens():
    carrinho = session["carrinho"]

    soma = 0

    for item in carrinho:
        preco = float(item["preco"])
        soma += preco
    
    return soma


def somar_preco_adicionais():
    carrinho = session["carrinho"]

    soma = 0

    for item in carrinho:
        adicionais = item["adicionais"]
        if adicionais:
            for adicional in adicionais:
                preco = float(adicional["preco"])

                # Caso não tenha a chave status (ela já vem por padrão false. Talvez esse tryblock seja desnecessário)
                try:
                   status = adicional["status"]
                   if status == "true":
                       soma += preco

                except Exception:
                    pass

    return soma


@pagamento_bp.route("/pagamento", methods=["POST", "GET"])
def pagamento():
    try:    
        return render_template("pagamento.html",
                            USER=session,
                            ITENS_CARRINHO=session['carrinho'],
                            QUANTIDADE_CARRINHO=len(session["carrinho"]),
                            SOMA_TOTAL = somar_preco_itens() + somar_preco_adicionais(),
                            ENTREGA = session["dados_entrega"])
    except Exception:
        return redirect(url_for("login.index"))