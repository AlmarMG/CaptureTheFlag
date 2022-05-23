from flask import redirect, url_for, render_template, request, session, flash
from flask_bcrypt import Bcrypt
import requests, re, json, sys, mariadb, docker
import webbrowser
from app import app

# bcrypt initializeren
bcrypt = Bcrypt(app)

# Captcha public key
captchaKey = "6Ld92oIaAAAAADR-q178z5dCb8TpHPKtuZ_kHWNS"

# Docker initializeren
client = docker.from_env()

# Illegale teken checker initializeren
checker = re.compile(r'[\W.]')


# --------------- database ---------------
try:
    conn = mariadb.connect(
        user="ITGirl",
        password="gm7fNbatwz",
        host="db",
        port=3306,
        database="Gegevens"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

conn.autocommit = True
cur = conn.cursor()


# --------------- losse functies ---------------

# Functie om de hash van een container te verkrijgen
def containerId(container):
    if client.containers.list(filters={'name': container}):
        id = client.containers.list(filters={'name': container})
        return str(id[0].id)[:12]
    else:
        return None


# Captcha functie 
def mens(captcha_response):
    secret = "6Ld92oIaAAAAAOg-_D1OJtaVAWVSeRaOFiU2kT8T"
    payload = {'response': captcha_response, 'secret': secret}
    response = requests.post("https://www.google.com/recaptcha/api/siteverify", payload)
    response_text = json.loads(response.text)
    return response_text['success']


# --------------- login pagina ---------------
@app.route("/", methods=["POST", "GET"])
def login():
    # Check of de gebruiker al is ingelogd, zo ja verbind door naar challenges pagina
    if 'loggedin' in session:
        flash("Je bent al ingelogd!", category="warning")
        return redirect(url_for('challenges'))
    
    if request.method == "POST":
        # Haal waardes uit form
        usernameForm = request.form["name"].lower()
        passwordForm = request.form["pass"]
        captchaResponse = request.form['g-recaptcha-response']

        # Check of username in database zit
        cur.execute("""
                    select gebruikersnaam, wachtwoord, id 
                    from Gebruiker 
                    where gebruikersnaam = %s
                    """, (usernameForm,))
        account = cur.fetchone()

        # Account bestaat niet, geef dit door aan de gebruiker
        if account is None:
            flash("De gebruikersnaam of wachtwoord is incorrect!", category="danger")
            return redirect(url_for("login"))

        # Account bestaat wel, haal de waardes uit de database op
        usernameDb = account[0]
        passwordDb = account[1]
        idDb = account[2]

        # Check of het wachtwoord correct is
        validation = bcrypt.check_password_hash(passwordDb, str(passwordForm))

        # Check of alle gegeven gegevens kloppen en de captcha ingevuld is
        if mens(captchaResponse) and account and usernameForm == usernameDb and validation:
            # Zet een paar waardes in de session
            session['name'] = usernameDb
            session['id'] = idDb
            session['loggedin'] = True

            # Haal de score van de gebruiker uit de database
            cur.execute("""
                        select sum(Challenge.score) as totaalScore
                        from ChallengeStatus
                        inner join Challenge on ChallengeStatus.challengeId = Challenge.id
                        where ChallengeStatus.gebruikerId = %s and ChallengeStatus.status = 1
                        """, (session["id"],))
            scoreGebruiker = cur.fetchone()[0]
            
            # Als er geen score terug komt van de database is de score dus 0
            if scoreGebruiker is None:
                session['score'] = 0   
            else:
                session['score'] = int(scoreGebruiker)
            
            # Haal hint waardes van de gebruiker uit de database
            cur.execute("""
                        select sum(Hint.waarde) 
                        from Hint
                        inner join HintStatus on Hint.id = HintStatus.hintId
                        where HintStatus.status = 1 and HintStatus.gebruikerId = %s
                        """, (session["id"],))
            waardeHints = cur.fetchone()[0]

            # Haal de waarde van de hints van de score af als er waardes zijn gevonden in de database
            if waardeHints is not None:
                session['score'] -= int(waardeHints)

            # Stuur de gebruiker door naar de challenges pagina
            flash("Successvol ingelogd!", category="success")
            return redirect(url_for("challenges"))

        # Het wachtwoord klopt niet, geef dit door aan de gebruiker
        elif not validation:
            flash("De gebruikersnaam of wachtwoord is incorrect!", category="danger")
            return redirect(url_for("login"))
        
        # De captcha is niet voltooid, geef dit door aan de gebruiker
        else:
            flash("De captcha moet voltooid worden om verder te gaan", category="warning")
            return redirect(url_for("login"))

    return render_template("login.html", sitekey=captchaKey)


# --------------- registreer pagina ---------------
@app.route("/registreer", methods=["POST", "GET"])
def account():
    # Check of de gebruiker al is ingelogd, zo ja verbind door naar challenges pagina
    if 'loggedin' in session:
        flash("Je bent al ingelogd!", category="warning")
        return redirect(url_for('challenges'))

    if request.method == "POST":
        # Haal waardes uit form
        usernameForm = request.form["name"].lower()
        passwordForm = request.form["pass"]
        passwordConfirm = request.form["passConf"]
        captchaResponse = request.form['g-recaptcha-response']

        # Hash het wachtwoord
        passwordHashed = bcrypt.generate_password_hash(passwordForm).decode('utf-8')

        # Check of username in database zit en haal deze op
        cur.execute("""
                    select gebruikersnaam 
                    from Gebruiker where gebruikersnaam = %s
                    """, (usernameForm,))
        usernameDb = cur.fetchone()

        # Username bestaat nog niet, voer nu overige checks uit
        if usernameDb is None:
            # Check of er illegale tekens worden gebruikt
            if checker.search(usernameForm) or checker.search(passwordForm) or checker.search(passwordConfirm):
                flash("Het invoerveld bevat illegale karakters", category="danger")
                return redirect(url_for("account"))

            # Check of de wachtwoorden overeenkomen
            elif passwordForm != passwordConfirm:
                flash("De wachtwoorden komen niet overeen", category="danger")
                return redirect(url_for("account"))

            # Check of de nieuwe username 50 of meer tekens bevat 
            elif len(usernameForm) > 50:
                flash("Je gebruikersnaam mag niet langer zijn dan 50 tekens", category="danger")
                return redirect(url_for("account"))    

            # Check of het wachtwoord tussen de 8 en 64 tekens zit
            elif not 8 < len(passwordForm) < 64:
                flash("Het wachtwoord moet tussen de 8 en 64 tekens liggen", category="danger")
                return redirect(url_for("account"))

            # Check of de captcha niet is ingevult
            elif not mens(captchaResponse):
                flash("De captcha moet voltooid worden om verder te gaan", category="warning")
                return redirect(url_for("account"))

            # Alles is goed, voeg de gebruiker toe in de database en redirect naar de login pagina
            else:
                # Voeg de username en wachtwoord toe aan de database
                cur.execute("""
                            insert into Gebruiker (gebruikersnaam, wachtwoord) 
                            values (%s, %s)
                            """, (usernameForm, passwordHashed,))
                
                # Haal het id van de nieuwe gebruiker op uit de database
                cur.execute("""
                            select id 
                            from Gebruiker 
                            where gebruikersnaam = %s
                            """, (usernameForm,))
                idDb = int(cur.fetchone()[0])
                
                # Haal de hoeveelheid challenges op uit de database
                cur.execute("""
                            select id
                            from Challenge
                            """)
                aantalChallenges = cur.fetchall()

                # Loop door de hoeveelheid challenges
                for challengeId in range(len(aantalChallenges)):
                    challengeId += 1
                    cur.execute("""
                                insert into ChallengeStatus (gebruikerId, challengeId, status)
                                values (%s, %s, 0)
                                """, (idDb, challengeId,))
                
                # Haal de hoeveelheid hints op uit de database
                cur.execute("""
                            select id
                            from Hint
                            """)
                aantalHints = cur.fetchall()
                
                # Loop door de hoeveelheid hints
                for hintId in range(len(aantalHints)):
                    hintId += 1
                    cur.execute("""
                                insert into HintStatus (hintId, gebruikerId, status)
                                values (%s, %s, 0)
                                """, (hintId, idDb,))
                
                # Account succesvol aangemaakt, geef dit door aan de gebruiker
                flash("Account succesvol aangemaakt!", category="success")
                return redirect(url_for("login"))

        # De username bestaat al, geef dit door aan de gebruiker
        flash("Deze gebruikersnaam bestaat al", category="warning")
        return redirect(url_for("account"))

    return render_template("account.html", sitekey=captchaKey)


# --------------- uitlog route ---------------
@app.route("/logout")
def logout():
    session.pop('loggedin', None)
    session.pop('name', None)
    session.pop('id', None)
    session.pop('score', None)
    flash("Successvol uitgelogd!", category="success")
    return redirect(url_for('login'))


# --------------- over ons pagina ---------------
@app.route("/over-ons")
def overons():
    # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina
    if 'loggedin' in session:
        return render_template("over-ons.html", gebruikersnaam=session['name'], score=session['score'])
    
    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))


# --------------- ranglijst pagina ---------------
@app.route("/ranglijst")
def ranglijst():
    # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina
    if 'loggedin' in session:
        # Haal alle gebruikersnamen en scores uit de database
        cur.execute ("""
                    select score.gebruikersnaam, score.score-waarde.waarde as totaal, score.id 
                    from (
                        Select (
                            (
                                select sum(Challenge.score) 
                                from Challenge
                            ) - sum(Challenge.score)) as score, Gebruiker.gebruikersnaam, Gebruiker.id from Gebruiker
                        inner join ChallengeStatus on ChallengeStatus.gebruikerId = Gebruiker.id 
                        inner join Challenge on ChallengeStatus.challengeId = Challenge.id
                        where ChallengeStatus.status = 0 group by Gebruiker.id) as score
                    inner join (
                        Select ((select sum(Hint.waarde) from Hint) - sum(Hint.waarde)) as waarde, Gebruiker.id 
                        from Gebruiker inner join HintStatus on HintStatus.gebruikerId = Gebruiker.id  
                        inner join Hint on HintStatus.hintId = Hint.id where HintStatus.status = 0 group by Gebruiker.id
                    ) as waarde on score.id = waarde.id 
                    group by score.id order by totaal desc
                    """)
        data = cur.fetchall()

        return render_template("ranglijst.html", gebruikersnaam=session['name'], score=session['score'], data=data)
    
    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))


# --------------- flagcheck pagina ---------------
@app.route("/flagcheck", methods=["POST", "GET"])
def flagcheck():
    # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina  
    if 'loggedin' in session:
        if request.method == "POST":
            # Haal de flag uit de form
            ingevuldeFlag = request.form['flag']
            # Haal challenge informatie uit de database
            cur.execute("""
                        select id, naam, score 
                        from Challenge 
                        where flag = %s
                        """, (ingevuldeFlag,))
            challenge = cur.fetchone()
            print(challenge)
            print(ingevuldeFlag)

            # Er is niks gevonden in de database dus de flag is fout
            if challenge is None:
                flash("De ingevoerde flag is fout", category="danger")
                return redirect(url_for('flagcheck'))
            
            # Zet database waardes in variabelen 
            challengeId = challenge[0]
            challengeNaam = challenge[1].lower()
            challengeScore = int(challenge[2])

            # Haal de status van een challenge van de gebruiker op uit de database
            cur.execute("""
                        select status 
                        from ChallengeStatus 
                        where gebruikerId = %s and challengeId = %s
                        """, (session['id'], challengeId,))
            status = int(cur.fetchone()[0])

            # De status is 0 dus de flag is nog niet gevonden
            if status == 0:
                # Voeg deze score toe aan de session score
                session['score'] += challengeScore

                # Update de status van de challenge, nu heeft de gebruiker de challenge voltooid
                cur.execute("""
                            update ChallengeStatus 
                            set status = 1 
                            where gebruikerId = %s and challengeId = %s
                            """, (session['id'], challengeId,))

                # Verwijder de container van de challenge
                cur.execute("""
                            delete from Container 
                            where gebruikerId = %s and challengeNaam = %s
                            """, (session['id'], challengeNaam ,))

                # Haal de container id op van docker            
                id = containerId(f"chal-{challengeNaam}_id-{session['id']}")

                # De id bestaat, verwijder nu de container
                if id is not None:
                    # Selecteer de container
                    container = client.containers.get(container_id=id)
                    # Sluit de container
                    container.stop(timeout=0)

                flash(f"Gefeliciteerd je hebt de {challengeNaam} challenge gehaald! Er worden nu {challengeScore} punten aan je score toegevoegd.", category="success")
                return redirect(url_for('flagcheck'))
            
            # De challenge is al eerder voltooid
            flash(f"De flag voor de {challengeNaam} challenge heb je al eerder gevonden!", category="warning")
            return redirect(url_for('flagcheck'))

        return render_template("flagcheck.html", gebruikersnaam=session['name'], score=session['score'])

    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))


# --------------- challenge pagina ---------------
@app.route("/challenges")
def challenges():
    # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina
    if 'loggedin' in session:
        # Haal de challenge gegevens en de status op uit de database
        cur.execute("""
                    select Challenge.id, Challenge.moeilijkheidsgraad, Challenge.naam, ChallengeStatus.status, Challenge.flaskNaam, HintPagina.flaskNaam 
                    from Challenge
                        inner join ChallengeStatus On Challenge.id = ChallengeStatus.challengeId
                        inner join HintPagina on Challenge.id = HintPagina.challengeId
                    where ChallengeStatus.gebruikerId = %s
                    """, (session['id'],))
        challengeLijst = cur.fetchall()

        return render_template("challenges.html", gebruikersnaam=session['name'], score=session['score'], challengeLijst=challengeLijst)

    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))
    


