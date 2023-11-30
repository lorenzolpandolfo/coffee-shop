from flask import Blueprint, render_template, redirect, session, url_for, request, jsonify
from crud_modules import firebase_settings
import json

editando_bp = Blueprint("editando", __name__, template_folder="templates")


@editando_bp.route("/editando", methods=["POST", "GET"])
def editando():
    if request.method == "GET":

        # recebendo uma alteração de item no carrinho
        checkbox_item_id = request.args.get('itemId')
        if checkbox_item_id:
            checkbox_adicional_id = request.args.get('adicionalId')
            checkbox_value = request.args.get('checkboxValue')

            session["carrinho"][int(checkbox_item_id) - 1]["adicionais"][int(checkbox_adicional_id) - 1]["status"] = checkbox_value
            session.modified = True

            print(session["carrinho"])
        
            # print(session["carrinho"][int(checkbox_item_id) - 1]["adicionais"])


    
    return render_template("editando.html",
                           USER=session,
                           ITENS_CARRINHO=session['carrinho'],
                           QUANTIDADE_CARRINHO=len(session["carrinho"]))