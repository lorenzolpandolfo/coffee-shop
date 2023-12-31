from flask import Flask
from blueprints.homepage.homepage import homepage_bp
from blueprints.login.login import login_bp
from blueprints.register.register import register_bp
from blueprints.carrinho.carrinho import carrinho_bp
from blueprints.pagamento.pagamento import pagamento_bp
from blueprints.editando.editando import editando_bp
from blueprints.entrega.entrega import entrega_bp
from blueprints.perfil.perfil import perfil_bp
from blueprints.registrarEndereco.reg_endereco import reg_endereco_bp
from blueprints.registrarCartao.reg_cartao import reg_cartao_bp

app = Flask(__name__)
app.secret_key = 'secret'

app.register_blueprint(homepage_bp)
app.register_blueprint(login_bp)
app.register_blueprint(register_bp)
app.register_blueprint(carrinho_bp)
app.register_blueprint(pagamento_bp)
app.register_blueprint(editando_bp)
app.register_blueprint(entrega_bp)
app.register_blueprint(perfil_bp)
app.register_blueprint(reg_endereco_bp)
app.register_blueprint(reg_cartao_bp)


if __name__ == '__main__':
    app.run(debug=True)
