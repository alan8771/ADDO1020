"teste"
from flask import Flask, render_template

app = Flask (__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/oi")
def outro():
    return render_template("oi")

@app.route("/usuarios/<nome_do_usuario>")
def usuarios(nome_do_usuario):
    return render_template("PF.html", nome_do_usuario=nome_do_usuario)

if __name__ == "__main__":
    app.run(debug=True)