from flask import Flask, redirect, url_for, render_template, request, session, flash
from app import app

# Het wachtwoord waarmee de gebruiker op de flag-pgina kan komen
wachtwoord = 'Appel'

@app.route("/")
def home():
    if "user" in session:
        return render_template("index.html")
    else:
        return redirect(url_for("login"))

@app.route("/login", methods=["POST","GET"])
def login():
    # Data from form
    if request.method == "POST":
        user = request.form["naam"]
        answ = request.form["ww"]
        session["user"] = user
        session["ww"] = wachtwoord
        
        # Returns flag page if user fills in correct password
        if wachtwoord in answ:
            return redirect(url_for("home"))
        else:
            # If the user didn't fill in the correct password, he get's returned to the start
            flash("Helaas, probeer het opnieuw.", category="warning")
            session.pop("user", None)
            return redirect(url_for("login"))
            
    else:
        if "user" in session:
            return redirect(url_for("home"))
        return render_template("login.html")
