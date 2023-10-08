from flask import Blueprint, render_template, redirect

homepage_bp = Blueprint("homepage", __name__, template_folder="templates")

@homepage_bp.route("/")
def index():
    return render_template("homepage.html")
    


@homepage_bp.route("/novidades")
def test():
    return 'Aqui estão as novidades do momento.'

