from flask import Flask, redirect, url_for, render_template, request, session, flash
from app import app

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = 'Alberto12'
        wachtwoord = 'test123'
        uname = request.form["uname"]
        wachtw = request.form["psw"]

        if username in uname and wachtwoord in wachtw or username in uname and session["ww"] in wachtw:
            session.pop("ww", None)
            return redirect(url_for("protected"))
        elif username != uname and wachtwoord != wachtw or username != uname and session["ww"] != wachtw:
            flash("Gebruikersnaam en Wachtwoord zijn niet correct, probeer het opnieuw", category="danger")
            return redirect(url_for("login"))   
        elif username != uname:
            flash("Gebruikersnaam was niet correct, probeer het opnieuw", category="danger")
            return redirect(url_for("login"))
        else:
            flash("Wachtwoord was niet correct, probeer het opnieuw", category="danger")
            return redirect(url_for("login"))
    else:
        return render_template("login.html")

@app.route("/forgot-password", methods=["POST", "GET"])
def forgot():
    if request.method == "POST":
        username = 'Alberto12'
        town = 'Emmen'
        uname = request.form["uname_forgot"]
        town_form = request.form["town_forgot"]
        wwoord = request.form["psw_forgot"]
        ww_confirm = request.form["psw_forgot2"]

        if username in uname and town in town_form and wwoord == ww_confirm:
            session["ww"] = wwoord
            flash(f"Wachtwoord succesvol veranderd", category="success")
            return redirect(url_for("login"))
        elif username != uname and town != town_form and wwoord != ww_confirm:
            flash("Gebruikersnaam, Geboorteplaats en Wachtwoorden kwamen niet overeen, probeer het opnieuw", category="danger")
            return redirect(url_for("forgot"))
        elif username != uname:
            flash("Gebruikersnaam was niet correct, probeer het opnieuw", category="danger")
            return redirect(url_for("forgot"))
        elif town != town_form:
            flash("Geboorteplaats was niet correct, probeer het opnieuw", category="danger")
            return redirect(url_for("forgot"))
        else:
            flash("Wachtwoorden kwamen niet overeen, probeer het opnieuw", category="danger")
            return redirect(url_for("forgot"))
        
    else:
        return render_template("forgot.html")

@app.route("/173edb66276f0227b2523d6ef7ca93bd44c78fabb92d36d738ad9c0429a71a06")
def protected():
    return render_template("protected.html")

@app.route("/")
def socialmedia():
    return render_template("socialmedia.html")

@app.route("/6a5800844860611cb761c82c8110afbbcfce5757526755b244c087e2dd40c15f")
def challenges():
    return redirect('https://itgirls-ctf.localhost/challenges', code=301) 
