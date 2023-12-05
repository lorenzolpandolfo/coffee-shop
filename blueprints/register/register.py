from flask import Blueprint, render_template, redirect, request, url_for, session
from crud_modules import firebase_settings

auth = firebase_settings.auth
admin_auth = firebase_settings.admin_auth
database = firebase_settings.admin_db

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
                # perdendo informações de antigas contas
                session.clear()
                # carrega o usuario na sessao
                session['user'] = auth.create_user_with_email_and_password(email, senha)
                
                localid = session['user']['localId']
                session["email"] = email
                
                new_user_data = {
                    "localid": localid,
                    "nome": nome,
                    "email": email,
                    "telefone": telefone
                }

                # salva no banco de dados as informações do usuario
                
                database.reference(f"/users/{localid}").update(new_user_data)
                return redirect(url_for("homepage.home"))

            except Exception as ERRO:
                if "EMAIL_EXISTS" in str(ERRO):
                    return render_template("register.html", erro = 'O email já está registrado')
                
                else:
                    return render_template("register.html", erro = ERRO)

    else:
        return render_template("register.html")
