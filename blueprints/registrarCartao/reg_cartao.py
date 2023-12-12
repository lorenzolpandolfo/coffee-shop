from flask import Blueprint, render_template, redirect, session, url_for, request, jsonify
from crud_modules import firebase_settings
from blueprints.registrarCartao import crypt_info
import json


database = firebase_settings.admin_db

reg_cartao_bp = Blueprint("reg_cartao", __name__, template_folder="templates")


@reg_cartao_bp.route("/registrar-cartao", methods=["POST", "GET"])
def reg_cartao():
    try:
        mylocalid = session['user']['localId']

        if request.method == "GET":
            numero_cartao = request.args.get('numero_cartao')
            validade = request.args.get('validade')
            cvv = request.args.get('cvv')
            titular = request.args.get('titular')
            cpf = request.args.get('cpf')
            apelido_cartao = request.args.get('apelido_cartao')

            if numero_cartao is not None:
                dc = {
                    "numero_cartao":    numero_cartao,
                    "validade":         validade,
                    "cvv":              cvv,
                    "titular":          titular,
                    "cpf":              cpf,
                    "apelido_cartao":   apelido_cartao
                }
                
                # criptografando os dados
                dc = crypt_info.encrypt_dict(dc)
                
                # enviando dados para o banco de dados
                database.reference(f"/users/{mylocalid}/cartoes").push().set(dc)
                

        return render_template("reg_cartao.html",
                            USER=session,
                            ITENS_CARRINHO=session['carrinho'],
                            QUANTIDADE_CARRINHO=len(session["carrinho"]))
    except Exception:
        return redirect(url_for("login.index"))
