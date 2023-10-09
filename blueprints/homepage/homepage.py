from flask import Blueprint, render_template, redirect, session, url_for

homepage_bp = Blueprint("homepage", __name__, template_folder="templates")

@homepage_bp.route("/")
def home():
    print(f"Session recebido no home: {session}")
    if session:
        return render_template("homepage.html", USER=session)
    else:
        return redirect(url_for("login.index"))
