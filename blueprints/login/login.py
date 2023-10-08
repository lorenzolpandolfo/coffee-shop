from flask import Blueprint, render_template, redirect

login_bp = Blueprint("login", __name__, template_folder="templates")

@login_bp.route("/login")
def index():
    return render_template("login.html")
