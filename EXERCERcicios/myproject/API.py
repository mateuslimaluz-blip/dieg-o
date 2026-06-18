from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "API funcionando!"

@app.route("/sobre")
def sobre():
    return "Esta é minha primeira API"

@app.route("/usuario/<nome>")
def usuario(nome):
    return f"Olá, {nome}!"

if __name__ == "__main__":
    app.run(debug=True)