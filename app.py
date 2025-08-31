from flask import Flask, render_template, url_for
from database import init_db

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
