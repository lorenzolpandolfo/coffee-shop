from flask import Blueprint, render_template, redirect, request, session, url_for
from crud_modules import firebase_settings


auth = firebase_settings.auth

login_bp = Blueprint("login", __name__, template_folder="templates")


@login_bp.route("/login", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        try:
            session.clear()
            # carrega o usuario na sessao
            session['user'] = auth.sign_in_with_email_and_password(email, senha)
            return redirect(url_for("homepage.home"))
        
        except Exception as ERRO:
                if "EMAIL_EXISTS" in str(ERRO):
                    return render_template("login.html", erro = "O email já está registrado")
                
                if "INVALID_LOGIN_CREDENTIALS" in str(ERRO):
                    return render_template("login.html", erro = "Credenciais inválidas")
                     
                else:
                    return render_template("login.html", erro = ERRO)
        
    else:
        return render_template("login.html")
