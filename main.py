from flask import Flask
from blueprints.homepage.homepage import homepage_bp
from blueprints.login.login import login_bp
from blueprints.register.register import register_bp

app = Flask(__name__)
app.secret_key = 'secret'

app.register_blueprint(homepage_bp)
app.register_blueprint(login_bp)
app.register_blueprint(register_bp)

if __name__ == '__main__':
    app.run(debug=True)