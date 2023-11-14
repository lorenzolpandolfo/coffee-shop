from flask import Blueprint, render_template, redirect, session, url_for, request, jsonify
import firebase_settings
import json

pagamento_bp = Blueprint("pagamento", __name__, template_folder="templates")


@pagamento_bp.route("/pagamento", methods=["POST", "GET"])
def pagamento():    
    return render_template("pagamento.html", USER=session, ITENS_CARRINHO=session['carrinho'], QUANTIDADE_CARRINHO=len(session["carrinho"]))