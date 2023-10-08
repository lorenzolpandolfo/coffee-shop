from flask import Flask
from blueprints.homepage.homepage import homepage_bp

app = Flask(__name__)

app.register_blueprint(homepage_bp)

if __name__ == '__main__':
    app.run(debug=True)