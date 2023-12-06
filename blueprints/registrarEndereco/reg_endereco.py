from flask import Blueprint, render_template, redirect, session, url_for, request, jsonify
from crud_modules import firebase_settings
import json

database = firebase_settings.admin_db

reg_endereco_bp = Blueprint("reg_endereco", __name__, template_folder="templates")


@reg_endereco_bp.route("/registrar-endereço", methods=["POST", "GET"])


def reg_endereco():
    try:

        mylocalid = session['user']['localId']

        if request.method == "GET":
            rua_value = request.args.get('rua_value')
            numero_value = request.args.get('numero_value')
            bairro_value = request.args.get('bairro_value')
            cep_value = request.args.get('cep_value')
            complemento_value = request.args.get('complemento_value')
            apelido_value = request.args.get('apelido_value')
            referencia_value = request.args.get('referencia_value')

            if cep_value:
                dc = {
                    "rua":          rua_value,
                    "numero":       numero_value,
                    "bairro":       bairro_value,
                    "cep":          cep_value,
                    "complemento":  complemento_value,
                    "apelido":      apelido_value,
                    "referencia":   referencia_value
                }

                print(dc)

                database.reference(f"/users/{mylocalid}/enderecos").push().set(dc)
                

        return render_template("reg_endereco.html",
                            USER=session,
                            ITENS_CARRINHO=session['carrinho'],
                            QUANTIDADE_CARRINHO=len(session["carrinho"]))
    except Exception:
        return redirect(url_for("login.index"))
