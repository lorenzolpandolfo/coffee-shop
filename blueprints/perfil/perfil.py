from flask import Blueprint, render_template, redirect, session, url_for, request, jsonify
from crud_modules import firebase_settings
import json
from blueprints.registrarCartao import crypt_info

database = firebase_settings.admin_db

perfil_bp = Blueprint("perfil", __name__, template_folder="templates")


def get_user_info(localId):
    usuarios = database.reference("/users").get()
    return usuarios[localId]


def consultar_enderecos(localId):
    enderecos = database.reference(f"/users/{localId}").child("enderecos").get()

    if enderecos:
        return enderecos


def consultar_cartoes(localId):
    # pega o nó dos cartoes
    cartoes = database.reference(f"/users/{localId}/cartoes").get()
    decrypted_cartoes = {}
    
    # se tiver cartoes
    if cartoes:
        # para cada id de cartao nos cartoes registrados na conta
        for cartaoId in cartoes:
            # consulta os dados do cartao
            cartao = database.reference(f"/users/{localId}/cartoes/{cartaoId}").get()
            
            cartao = crypt_info.decrypt_dict(cartao)
            decrypted_cartoes[cartaoId] = cartao

        return decrypted_cartoes


@perfil_bp.route("/perfil", methods=["POST", "GET"])
def perfil():
    try:
        user = session["user"]
        mylocalid = session["user"]["localId"]

    except Exception:
        return redirect(url_for("login.index"))
        

    if request.method == "GET":
        endereco_id = request.args.get('endereco_id')
        cartao_id = request.args.get('cartao_id')
        
        if endereco_id:
            database.reference(f"/users/{mylocalid}/enderecos").child(endereco_id).delete()
        

        if cartao_id:
            database.reference(f"/users/{mylocalid}/cartoes").child(cartao_id).delete()
    


    if request.method == "POST":
        funcao = request.form["sair"]
        
        if funcao:
            session.clear()
            return redirect(url_for("login.index"))
            

    user = get_user_info(mylocalid)
    return render_template("perfil.html",
                        USER=user,
                        ITENS_CARRINHO=session['carrinho'],
                        QUANTIDADE_CARRINHO=len(session["carrinho"]),
                        ENDERECOS=consultar_enderecos(mylocalid),
                        CARTOES=consultar_cartoes(mylocalid))
