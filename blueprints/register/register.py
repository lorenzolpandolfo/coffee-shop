from flask import Blueprint, render_template, redirect, request, url_for, session
import crud
import user as class_user

db = crud.database
auth = crud.auth

register_bp = Blueprint("register", __name__, template_folder="templates")

@register_bp.route("/registrar-se", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        nome = request.form["nome"]
        senha = request.form["senha"]
        telefone = request.form["telefone"]

        # Tem que conferir se o email ja nao ta registrado manualmente. Ou entao pegar o erro que o Firebase retorna
        if len(senha) < 6:
            return render_template("register.html", erro = "A senha deve ser maior do que 6 caracteres.")
        else:
            try:
                user = auth.create_user_with_email_and_password(email, senha)
                session["user"] = auth.get_account_info(user["idToken"])
                mynewuser = class_user.User(session['user']['users'][0]['localId'], nome, email, telefone)
                
                db.child("users").update({mynewuser.nome:mynewuser.toDict()})
                class_user.myuser = mynewuser
                return redirect(url_for("homepage.home"))
            
            except Exception as ERRO:
                return render_template("register.html", erro = ERRO)

    else:
        return render_template("register.html")

