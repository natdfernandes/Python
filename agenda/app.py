import os

from flask import Flask
from routes import routes, db

app = Flask(__name__)
app.register_blueprint(routes)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


# verifica se o banco de dados existe e cria a tabela se necessario
#
def create_db():
    if not os.path.exists("database.db"):
        with app.app_context():
            db.create_all()  # cria a(s) tabela(s)


create_db()  # chama a função para verificar e criar o banco de dados
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
