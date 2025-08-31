from flask import Flask

# cria a aplicação Flask
app = Flask(__name__)

# rota principal (home)
@app.route("/")
def home():
    return "Olá, mundo! Meu primeiro servidor Flask."

# só roda se executar este arquivo diretamente
if __name__ == "__main__":
    app.run(debug=True)
