from flask import Blueprint, render_template, redirect, session, url_for
import firebase_settings

carrinho_bp = Blueprint("carrinho", __name__, template_folder="templates")


@carrinho_bp.route("/carrinho")
def carrinho():
    return render_template("carrinho.html", ITENS_CARRINHO=session['carrinho'])