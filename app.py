from flask import Flask, render_template, url_for, request, redirect
from flask_mysqldb import MySQL
from credentials import credentials
import hashlib

app = Flask(__name__)

app.config['MYSQL_HOST'] = credentials['host']
app.config['MYSQL_USER'] = credentials['user']
app.config['MYSQL_PASSWORD'] = credentials['password']
app.config['MYSQL_DB'] = credentials['db']

mysql = MySQL(app)

user_pages = {
    'profil':       'Informations générales',
    'adresse':      'Adresse de livraison',
    'security':     'Connexion et sécurité',
    'contact':      'Contact'
}

@app.route("/")
def home():
    return render_template("index.html", title = "Page d'accueil")

@app.route("/profil")
def profil():
    return render_template("profil.html", title = "Profil", pages = user_pages)

@app.route("/adresse")
def adresse():
    if request.method == 'POST':
        return redirect('/')
    else:
        return render_template("contact.html", title = "Adresse de livraison", pages = user_pages)

@app.route("/information", methods = ['GET', 'POST'])
def security():
    if request.method == 'POST':
        return redirect('/')
    else:
        return render_template("contact.html", title = "Connexion et sécurité", pages = user_pages)

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        print(request.form['sujet'])
        print(request.form['message'])
        sujet = request.form.get('sujet')
        msg = request.form.get('message')
        print(msg)
        return render_template("message.html", title = "Réponse", sujet = sujet, message = msg, pages = user_pages)
    else:
        return render_template("contact.html", title = "Contact", pages = user_pages)

@app.route("/register", methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        # register user...
        param = request.form
        # check existing address if so, retrieve the id, otherwise


        print(hashlib.sha256((param['email'] + ':' + param['password']).encode()).hexdigest())

        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            INSERT INTO users (address,firstName,lastName,email,pwd,phone) VALUES (?,?,?,?,?,?)
            """,
            param['address'],
            param['firstname'],
            param['lastname'],
            param['email'],
            param['password'],
            hashlib.sha256((param['email'] + ':' + param['password']).encode()).hexdigest()
        )
    else:
        return render_template("register.html", title = "Inscription", pages = user_pages)
if __name__ == '__main__':
    app.run(debug = True)