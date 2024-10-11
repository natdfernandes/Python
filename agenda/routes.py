from flask import Blueprint, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

routes = Blueprint("routes", __name__)
db = SQLAlchemy()


class Contact(db.Model):
    __tablename__ = "agenda"  # nome da tabela
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False)


@routes.route("/")
def index():
    contacts = Contact.query.all()
    return render_template("list.html", contacts=contacts)


@routes.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_contact = Contact(
            name=letra_maiscula(request.form["name"]),
            phone=request.form["phone"],
            email=request.form["email"],
        )
        db.session.add(new_contact)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add.html")


@routes.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    contact = Contact.query.get_or_404(id)
    if request.method == "POST":
        contact.name = letra_maiscula(request.form["name"])
        contact.phone = request.form["phone"]
        contact.email = request.form["email"]
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit.html", contact=contact)


@routes.route("/delete/<int:id>")
def delete(id):
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for("index"))


def letra_maiscula(nome):

    nome_lista = nome.split()
    print(type(nome), type(nome.split()))

    nova_lista = []

    for palavra in nome_lista:
        if palavra == "de" or palavra == "da" or palavra == "do":
            nova_lista.append(palavra)
            continue
        print(palavra)
        texto_capitalizado = palavra.capitalize()
        nova_lista.append(texto_capitalizado)
        print(texto_capitalizado)
    print(nova_lista)
    novo_nome = " ".join(nova_lista)
    print(novo_nome)
    return novo_nome
