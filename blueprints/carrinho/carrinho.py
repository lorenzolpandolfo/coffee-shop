from flask import Blueprint, render_template, redirect, session, url_for, request, jsonify
import firebase_settings
import json

carrinho_bp = Blueprint("carrinho", __name__, template_folder="templates")


@carrinho_bp.route("/carrinho", methods=["POST", "GET"])
def carrinho():
    if request.method == "GET":
        button_value = request.args.get('item')
        print(button_value)
        # Removendo item do carrinho
        if button_value:
            item = button_value.replace("'", '"').replace("True", "true").replace("False", "false")
            item = json.loads(item)

            # print(session["carrinho"])
            print('removendo ', item)
            session["carrinho"].remove(item)
            session.modified = True

            return jsonify({'quantidade_carrinho': len(session["carrinho"])})
            
    
        checkbox_item_id = request.args.get('itemId')
        if checkbox_item_id:
            checkbox_adicional_id = request.args.get('adicionalId')
            checkbox_value = request.args.get('checkboxValue')

            session["carrinho"][int(checkbox_item_id) - 1]["adicionais"][int(checkbox_adicional_id) - 1]["status"] = checkbox_value
            session.modified = True
        
            # print(session["carrinho"][int(checkbox_item_id) - 1]["adicionais"])


    
    return render_template("carrinho.html",
                           USER=session,
                           ITENS_CARRINHO=session['carrinho'],
                           QUANTIDADE_CARRINHO=len(session["carrinho"]))