from flask import Blueprint, render_template, redirect, session, url_for
import crud

homepage_bp = Blueprint("homepage", __name__, template_folder="templates")


def get_item_data():
    database = crud.database
    # print(database.child('itens').get().val()['Capuccino'])
    return database.child('itens').get().val()


@homepage_bp.route("/")
def home():
    print(f"Session recebido no home: {session}")
    if session:
        return render_template("homepage.html", USER=session, ITENS_CARDAPIO=get_item_data())
    else:
        return render_template("homepage.html", USER=False, ITENS_CARDAPIO=get_item_data())
