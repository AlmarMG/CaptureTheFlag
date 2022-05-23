from flask import redirect, url_for, render_template, request, flash, session
from app import app
import datetime

# --- Main pagina ---
@app.route("/")
def main():
    if "betalingscode" in session:
        return redirect(url_for("flag"))
    elif "scherm2" in session:
        return redirect(url_for("scherm3"))
    elif "scherm1" in session:
        return redirect(url_for("scherm2"))
    else:
        return redirect(url_for("scherm1"))

# --- Deel 1 ---
@app.route("/34f142b8ef61130e4a5d3b2c38ead5c1d6965f7d1560e813b1f27c045a1ab50b", methods=["POST","GET"])
def scherm1():
    # Decimale en hex nummer definiëren
    number = 62829
    numberHex = hex(number)

    # Check of je op de pagina mag zijn zo niet stuur terug naar main
    if "scherm1" in session or "scherm2" in session or "betalingscode" in session:
        return redirect(url_for("main"))
    
    elif request.method == "POST":
        # Trigger exception als er eerder een post request komt dan dat de code is ingevult
        try:
            codeInput = request.form["code"].lower()
            # Haal waardes op uit het scherm
            nameInput = request.form["name"]
           

            # Zet de username in de session
            session["username"] = nameInput

            # Check of de input van de code overeenkomt met code
            if codeInput == numberHex:
                session["scherm1"] = True
                session["code"] = numberHex
                return redirect(url_for("scherm2"))
        
        except:
            return redirect(url_for("scherm1"))

    return render_template("chat1.html", number=number)

# --- Deel 2 ---
@app.route("/88b95ad824f2ca306d2a5b71bd4c1907d68150abc2e1a2f9fb8fe74dfb079b7d", methods=["POST","GET"])
def scherm2():

    # Check of je op de pagina mag zijn zo niet stuur terug naar main
    if not "scherm1" in session or "scherm2" in session or "betalingscode" in session:
        return redirect(url_for("main"))
    
    elif request.method == "POST":
        # Trigger exception als er eerder een post request komt dan dat de log is ingevult
        try:
            logMogelijkheden = ["/shop/", "/shop", "shop/", "shop"]
            # Haal waardes op uit de chat
            log = request.form["log"].lower()

            # Check of de ingevulde log overeenkomt met de mogelijkheden
            if log in logMogelijkheden:
                session.pop("scherm1", None)
                session["scherm2"] = True
                return redirect(url_for("scherm3"))

        except:
            return redirect(url_for("scherm2"))

    return render_template("chat2.html", name=session["username"], code=session["code"])

@app.route("/gevoelig/logs/", methods=["POST","GET"])
def logs():
    if request.method == "POST":

        # Kaarthouder naam in de session zetten
        session["CC-naamKaarthouder"] = "James C. Town"
        # Flash een bericht als er op de resfresh knop wordt geklikt op de pagina
        flash(f"Refreshen niet toegestaan. Niet ondersteunde code in gebruik: {session['code']}")
        

    # Datum onderdelen maken voor op de site
    datum = datetime.date.today() + datetime.timedelta(days=73)
    datumFormat = datum.strftime("%d/%b/%Y")

    return render_template("logs.html", datum=datumFormat)

@app.route("/shop/", methods=["POST","GET"])
def shop():
    # betalingscode definiëren
    betalingscode = 7654729

    if request.method == "POST":
        # Lijsten aanmaken: 1 voor input, 1 voor antwoorden en 1 voor de onderdelen
        invoerLijst = []
        antwoordLijst = ["James C. Town", "5956272601707993", "503", "2026", "maart"]
        onderdeelLijst = ["Naam kaarthouder", "Creditcardnummer", "CVV/veiligheidsnummer", "Verval datum: Jaar", "Verval datum: Maand"]

        # Haal waardes op uit form
        kaarthouder = request.form["kaarthouder"].rstrip()
        creditcardnummer = request.form["creditcardnummer"]
        cvv = request.form["cvv"]
        jaar = request.form["jaar"].rstrip()
        maand = request.form["maand"].rstrip().lower()

        # Voeg alle waardes toe aan de invoer lijst
        invoerLijst.extend([kaarthouder, creditcardnummer, cvv, jaar, maand])

        # Check of alles klopt wat is ingevult, zo niet geef dit door aan de gebruiker
        for antwoord, onderdeel, invoer in zip(antwoordLijst,onderdeelLijst, invoerLijst):
            if antwoord != invoer:
                flash(f"Betaling onsuccesvol: de invoer '{onderdeel}' is incorrect", category="danger")
                return redirect(url_for("shop"))
        
        # Voeg de betalingscode toe aan de session en geef deze aan de gebruiker
        session["betalingscode"] = str(betalingscode)
        flash(f"Betaling succesvol: betalingscode: {betalingscode}", category="success")

    return render_template("form.html")

# Vier overige directpries
@app.route("/shop/cache/")
def shop_cache():
    return render_template("form_cache.html")

@app.route("/secret/")
def secret():
    return render_template("denied.html")

@app.route("/secret/vault/")
def secret_vault():
    return render_template("denied2.html")

@app.route("/unimportant/creditcard/")
def unimportant_card():
    return render_template("card.html")

# --- Deel 3 ---
@app.route("/77666224bed6809977958ae1c98c513c5ae867b4c024d87e6e49f59fd3639e3d", methods=["POST","GET"])
def scherm3():
    # Check of je op de pagina mag zijn zo niet stuur terug naar main
    if not "scherm2" in session or "scherm1" in session or "betalingscode" in session:
        return redirect(url_for("main"))

    elif request.method == "POST":
        # Haal de betalingscode uit de chat op
        formBetalingscode = request.form["betalingscode"]

        # Trigger exception als er geen betalingscode in session is
        try:
            # Check of de betalingscode correct is
            if formBetalingscode == session["betalingscode"]:
                return redirect(url_for("flag"))
        except KeyError:
            return redirect(url_for("main"))

    return render_template("chat3.html")

@app.route("/gevoelig/lijst/")
def lijst():
    # Check of je op de pagina mag zijn zo niet stuur terug naar main
    if not "scherm2" in session or "scherm1" in session or "betalingscode" in session:
        return redirect(url_for("main"))    
    return render_template("lijst.html", name=session["username"])


# --- Deel 4 ---

@app.route("/127123d8e66436044134f8e3de4d00fea0ac8de9280f8821127c538ab0924620")
def flag():
    # Check of je op de pagina mag zijn zo niet stuur terug naar main
    if not "betalingscode" in session:
        return redirect(url_for("main"))
    return render_template("congrats.html")
