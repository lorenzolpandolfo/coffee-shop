from flask import Blueprint, render_template, redirect, session, url_for, request, jsonify
from crud_modules import firebase_settings
import json

database = firebase_settings.admin_db

perfil_bp = Blueprint("perfil", __name__, template_folder="templates")


def get_user_info(localId):
    usuarios = database.reference("/users").get()
    return usuarios[localId]


def consultar_enderecos(localId):
    enderecos = database.reference(f"/users/{localId}").child("enderecos").get()

    if enderecos:
        return database.reference(f"/users/{localId}").child("enderecos").get()
    else:
        return []

@perfil_bp.route("/perfil", methods=["POST", "GET"])
def perfil():
    mylocalid = session["user"]["localId"]

    if request.method == "GET":
        endereco_id = request.args.get('endereco_id')
        print(endereco_id)
        if endereco_id:
            database.reference(f"/users/{mylocalid}/enderecos").child(endereco_id).delete()
    

    user = get_user_info(mylocalid)
    print(user)
    return render_template("perfil.html",
                           USER=user,
                           ITENS_CARRINHO=session['carrinho'],
                           QUANTIDADE_CARRINHO=len(session["carrinho"]),
                           ENDERECOS=consultar_enderecos(mylocalid))