from flask import Blueprint, render_template, redirect, session, url_for, request, jsonify
from crud_modules import firebase_settings
import json

entrega_bp = Blueprint("entrega", __name__, template_folder="templates")

database = firebase_settings.admin_db


@entrega_bp.route("/entrega", methods=["POST", "GET"])
def entrega():
    try:
        mylocalid = session["user"]["localId"]

        if request.method == "GET":
            id = request.args.get("id")
            data = request.args.get("data")

            if data is not None and id is not None:
                data = str(request.args.get("data")).replace("'", '"').replace("True", "true").replace("False", "false")
                data = json.loads(data)

                session["dados_entrega"] = data
                session["id_entrega"] = id
                session.modified = True

                # Envia pro jquery a confirmação de que carregou a informação na sessão
                # depois disso, o jquery redireciona pra pagina de pagamento
                if session["dados_entrega"] == data:
                    return jsonify({"status":"sucesso"})

        return render_template("entrega.html",
                            USER=session,
                            ITENS_CARRINHO=session['carrinho'],
                            QUANTIDADE_CARRINHO=len(session["carrinho"]),
                            LOJAS=database.reference("/stores/").get(),
                            ENDERECOS=database.reference(f"/users/{mylocalid}/enderecos/").get())
    
    except Exception:
        return redirect(url_for("login.index"))
    