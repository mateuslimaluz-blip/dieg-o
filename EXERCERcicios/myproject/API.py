from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Bem-vindo ISSO DEU CERTO"

@app.route("/curso")
def curso():
    return "ANALISE e sistem"

@app.route("/escola")
def escola():
    return "CEP PEDRO BOARERO NELO"

if __name__ == "__main__":
    app.run(debug=True)
