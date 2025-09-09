from __init__ import app, db
from flask import render_template, request, redirect, url_for
from models import Livros
from Tools import Validate, Safe_Remove
from os import system as sy

@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        lista1 = []
        lista2 = []
        lista = list(db.session.query(Livros.titulo, Livros.historia).all())

        for i in lista:
            lista1.append(i[0])
            lista2.append(i[1])

        titulo_conto = list(zip(lista1, lista2))

        return render_template("index.html", titulo_conto=titulo_conto)
    
@app.route("/create", methods=["GET", "POST"])
def Criar_conto():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        historia = Validate(request.form.get("conto"))
        novo_livro = Livros(titulo=titulo, historia=historia)
        try:
            db.session.add(novo_livro)
            db.session.commit()
            return redirect(url_for("home"))
        except:
            return redirect(url_for("home"))

    if request.method == "GET":
        return render_template("create.html")

@app.route("/delete", methods=["GET", "POST"])
def Deletar_conto():
    if request.method == "POST":
        conto_delete = request.form.get("contoId")
        conto = Livros.query.filter_by(titulo=conto_delete).first()

        if conto:
            db.session.delete(conto)
            db.session.commit()
            return redirect(url_for("home"))
        else:
            return redirect(url_for("home"))

    if request.method == "GET":
        return render_template("delete.html")
    
@app.route("/update/<conto>", methods=["GET", "POST"])
def Atualizar_conto(conto):
    if request.method == "POST":
        novo_titulo = request.form.get("titulo")
        novo_conto = request.form.get("conto")
        novo_conto = Safe_Remove(novo_conto)
        novo_conto = Validate(novo_conto)

        # Tenho que dar um jeito nessa familia de if skskksksksksk
        if novo_titulo != "" and novo_conto != "":
            Livros.query.filter_by(historia=conto).update({Livros.titulo:novo_titulo, Livros.historia:novo_conto})
            db.session.commit()
            return redirect(url_for("home"))
        elif novo_titulo != "" and novo_conto == "":
            Livros.query.filter_by(historia=conto).update({Livros.titulo:novo_titulo})
            db.session.commit()
            return redirect(url_for("home"))
        elif novo_titulo == "" and novo_conto != "":
            Livros.query.filter_by(historia=conto).update({Livros.historia:novo_conto})
            db.session.commit()
            return redirect(url_for("home"))
        else:
            return redirect(url_for("home"))
    
    if request.method == "GET":
        return render_template("update.html", conto=conto)