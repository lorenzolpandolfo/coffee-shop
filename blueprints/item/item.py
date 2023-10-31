from flask import Blueprint, render_template, redirect, session, url_for
import firebase_settings

item_bp = Blueprint("item", __name__, template_folder="templates")


@item_bp.route("/item/<nome>")
def item(nome):
    return render_template("item.html", item=nome)