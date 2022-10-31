from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title = "Page d'accueil")

@app.route("/contact")
def contact():
    return render_template("contact.html", title = "Contact")