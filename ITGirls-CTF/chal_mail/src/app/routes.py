from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from app import app

# Configureer mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "itgirlsctf123@gmail.com"
app.config['MAIL_PASSWORD'] = "ITGirls.ctf12345"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# Mail initializeren
mail = Mail(app)

# Gebruiker kijgt dashboard te zien
@app.route("/", methods=["POST", "GET"])
def home():
    # opties die worden gebruikt in het formulier
    data = ['Vakantiefoto', 'Positieve coronatest', 'Logfiles', '30 gratis studiepunten']
    selected_user = request.form.get('lijst', None)

    if request.method == 'POST' and selected_user == 'Logfiles':
        flash("Veel succes", category="success")
        print(selected_user)
    # De gebruiker krijgt een mail toegestuurd
        email = request.form['email']
        subject = 'Wachtwoordaanvraag'
        msg = "Beste gebruiker, hierbij ontvang je jouw wachtwoord."

        message = Message(subject=subject, sender="itgirlsctf123@gmail.com", recipients=[email], body=msg)

        with app.open_resource("flag.pdf") as fp:
            message.attach("flag.pdf", "application/pdf", fp.read())

        mail.send(message)
    # Als de gebruiker een verkeerde optie heeft geselecteerd
    if request.method == 'POST' and selected_user != 'Logfiles':
        print("Test")
        flash("Helaas, probeer het opnieuw.", category="warning")
    
    return render_template("index.html", data=data)
