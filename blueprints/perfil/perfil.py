from flask import Blueprint, render_template, redirect, session, url_for, request, jsonify
from crud_modules import firebase_settings
import json

database = firebase_settings.admin_db

perfil_bp = Blueprint("perfil", __name__, template_folder="templates")


def get_user_info(localId):
    usuarios = database.reference("/users").get()
    return usuarios[localId]


@perfil_bp.route("/perfil", methods=["POST", "GET"])
def perfil():
    user = get_user_info(session["user"]["localId"])
    print(user)
    return render_template("perfil.html", USER=user, ITENS_CARRINHO=session['carrinho'], QUANTIDADE_CARRINHO=len(session["carrinho"]))