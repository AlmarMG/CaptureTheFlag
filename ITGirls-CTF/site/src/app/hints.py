from flask import redirect, url_for, render_template, request, session, flash, Blueprint
import mariadb, sys

# Blueprint aanmaken
hints = Blueprint('hints', __name__, template_folder='templates')


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


# --------------- hints ---------------
# --------------- moeilijk ---------------
@hints.route("/hints_moeilijk", methods=["POST", "GET"])
def hints_moeilijk():
    # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina  
    if 'loggedin' in session:
        # Haal de hint titel en beschrijving uit de database, dit wordt laten zien als je op de pagina komt
        cur.execute("""
                    select Hint.titel, Hint.beschrijving 
                    from Hint
                        inner join HintStatus on Hint.id = HintStatus.hintId
                    where Hint.hintPaginaId = 1 
                        and HintStatus.status = 1 
                        and HintStatus.gebruikerId = %s
                    """, (session["id"],)) 
        table = cur.fetchall()

        if request.method == "POST":
            # Haal de hintStatus, id, titel, gebruikerId en waarde uit de database
            cur.execute("""
                        select Hint.id, Hint.titel, Hint.waarde 
                        from Hint
                            inner join HintStatus on Hint.id = HintStatus.hintId
                        where Hint.hintPaginaId = 1 
                            and HintStatus.status = 0 
                            and HintStatus.gebruikerId = %s
                        """, (session["id"],)) 
            data = cur.fetchone()

            # Alle hints zijn al ontvangen, geef dit door aan de gebruiker
            if data is None:
                flash("Je hebt alle hints al ontvangen", category="danger")
                return redirect(url_for("hints.hints_moeilijk"))

            # Zet database waardes in variabelen
            hintIdDb = data[0]
            hintTitelDb = data[1]
            hintWaardeDb = data[2]

            # Check of de gebruiker genoeg punten heeft, zo ja haal de hint waarde van de score af
            if session["score"] >= hintWaardeDb:
                # Score min hintwaarde
                session["score"] -= hintWaardeDb

                # Update de hintstatus in de database
                cur.execute("""
                            update HintStatus 
                            set status = 1 
                            where hintId = %s and gebruikerId = %s
                            """, (hintIdDb, session["id"],))
                
                flash(f"Je hebt {hintTitelDb} ontvangen, er zijn {hintWaardeDb} punten afgetrokken van je score", category="success")
                return redirect(url_for("hints.hints_moeilijk"))
            
            # Laat de gebruiker weten dat hij/zij niet genoeg punten in bezit heeft
            flash("Je hebt niet genoeg punten om een hint te ontvangen", category="danger")
            return redirect(url_for("hints.hints_moeilijk"))
        
        return render_template("hints/hints_moeilijk.html", gebruikersnaam=session['name'], score=session['score'], results=table)
    
    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))


# --------------- cookie ---------------
@hints.route("/hints_cookie", methods=["POST", "GET"])
def hints_cookie():
     # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina  
    if 'loggedin' in session:
        # Haal de hint titel en beschrijving uit de database, dit wordt latenzien als je op de pagina komt
        cur.execute("""
                    select Hint.titel, Hint.beschrijving 
                    from Hint
                        inner join HintStatus on Hint.id = HintStatus.hintId
                    where Hint.hintPaginaId = 2 
                        and HintStatus.status = 1 
                        and HintStatus.gebruikerId = %s
                    """, (session["id"],)) 
        table = cur.fetchall()

        if request.method == "POST":
            # Haal de hintStatus, id, titel, gebruikerId en waarde uit de database
            cur.execute("""
                        select Hint.id, Hint.titel, Hint.waarde 
                        from Hint
                            inner join HintStatus on Hint.id = HintStatus.hintId
                        where Hint.hintPaginaId = 2
                            and HintStatus.status = 0 
                            and HintStatus.gebruikerId = %s
                        """, (session["id"],)) 
            data = cur.fetchone()

            # Alle hints zijn al ontvangen, geef dit door aan de gebruiker
            if data is None:
                flash("Je hebt alle hints al ontvangen", category="danger")
                return redirect(url_for("hints.hints_cookie"))

            # Zet database waardes in variabelen
            hintIdDb = data[0]
            hintTitelDb = data[1]
            hintWaardeDb = data[2]

            # Check of de gebruiker genoeg punten heeft, zo ja haal de hint waarde van de score af
            if session["score"] >= hintWaardeDb:
                # Score min hintwaarde
                session["score"] -= hintWaardeDb

                # Update de hintstatus in de database
                cur.execute("""
                            update HintStatus 
                            set status = 1 
                            where hintId = %s and gebruikerId = %s
                            """, (hintIdDb, session["id"],))
                
                flash(f"Je hebt {hintTitelDb} ontvangen, er zijn {hintWaardeDb} punten afgetrokken van je score", category="success")
                return redirect(url_for("hints.hints_cookie"))
            
            # Laat de gebruiker weten dat hij/zij niet genoeg punten in bezit heeft
            flash("Je hebt niet genoeg punten om een hint te ontvangen", category="danger")
            return redirect(url_for("hints.hints_cookie"))
        
        return render_template("hints/hints_cookie.html", gebruikersnaam=session['name'], score=session['score'], results=table)
    
    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))


# --------------- encodedchat ---------------
@hints.route("/hints_encodedchat", methods=["POST", "GET"])
def hints_encodedchat():
    # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina  
    if 'loggedin' in session:
        # Haal de hint titel en beschrijving uit de database, dit wordt latenzien als je op de pagina komt
        cur.execute("""
                    select Hint.titel, Hint.beschrijving 
                    from Hint
                        inner join HintStatus on Hint.id = HintStatus.hintId
                    where Hint.hintPaginaId = 3 
                        and HintStatus.status = 1 
                        and HintStatus.gebruikerId = %s
                    """, (session["id"],)) 
        table = cur.fetchall()

        if request.method == "POST":
            # Haal de hintStatus, id, titel, gebruikerId en waarde uit de database
            cur.execute("""
                        select Hint.id, Hint.titel, Hint.waarde 
                        from Hint
                            inner join HintStatus on Hint.id = HintStatus.hintId
                        where Hint.hintPaginaId = 3 
                            and HintStatus.status = 0 
                            and HintStatus.gebruikerId = %s
                        """, (session["id"],)) 
            data = cur.fetchone()

            # Alle hints zijn al ontvangen, geef dit door aan de gebruiker
            if data is None:
                flash("Je hebt alle hints al ontvangen", category="danger")
                return redirect(url_for("hints.hints_encodedchat"))

            # Zet database waardes in variabelen
            hintIdDb = data[0]
            hintTitelDb = data[1]
            hintWaardeDb = data[2]

            # Check of de gebruiker genoeg punten heeft, zo ja haal de hint waarde van de score af
            if session["score"] >= hintWaardeDb:
                # Score min hintwaarde
                session["score"] -= hintWaardeDb

                # Update de hintstatus in de database
                cur.execute("""
                            update HintStatus 
                            set status = 1 
                            where hintId = %s and gebruikerId = %s
                            """, (hintIdDb, session["id"],))
                
                flash(f"Je hebt {hintTitelDb} ontvangen, er zijn {hintWaardeDb} punten afgetrokken van je score", category="success")
                return redirect(url_for("hints.hints_encodedchat"))
            
            # Laat de gebruiker weten dat hij/zij niet genoeg punten in bezit heeft
            flash("Je hebt niet genoeg punten om een hint te ontvangen", category="danger")
            return redirect(url_for("hints.hints_encodedchat"))
        
        return render_template("hints/hints_encodedchat.html", gebruikersnaam=session['name'], score=session['score'], results=table)
    
    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))


# --------------- mail ---------------
@hints.route("/hints_mail", methods=["POST", "GET"])
def hints_mail():
    # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina  
    if 'loggedin' in session:
        # Haal de hint titel en beschrijving uit de database, dit wordt latenzien als je op de pagina komt
        cur.execute("""
                    select Hint.titel, Hint.beschrijving 
                    from Hint
                        inner join HintStatus on Hint.id = HintStatus.hintId
                    where Hint.hintPaginaId = 4 
                        and HintStatus.status = 1 
                        and HintStatus.gebruikerId = %s
                    """, (session["id"],)) 
        table = cur.fetchall()

        if request.method == "POST":
            # Haal de hintStatus, id, titel, gebruikerId en waarde uit de database
            cur.execute("""
                        select Hint.id, Hint.titel, Hint.waarde 
                        from Hint
                            inner join HintStatus on Hint.id = HintStatus.hintId
                        where Hint.hintPaginaId = 4 
                            and HintStatus.status = 0 
                            and HintStatus.gebruikerId = %s
                        """, (session["id"],)) 
            data = cur.fetchone()

            # Alle hints zijn al ontvangen, geef dit door aan de gebruiker
            if data is None:
                flash("Je hebt alle hints al ontvangen", category="danger")
                return redirect(url_for("hints.hints_mail"))

            # Zet database waardes in variabelen
            hintIdDb = data[0]
            hintTitelDb = data[1]
            hintWaardeDb = data[2]

            # Check of de gebruiker genoeg punten heeft, zo ja haal de hint waarde van de score af
            if session["score"] >= hintWaardeDb:
                # Score min hintwaarde
                session["score"] -= hintWaardeDb

                # Update de hintstatus in de database
                cur.execute("""
                            update HintStatus 
                            set status = 1 
                            where hintId = %s and gebruikerId = %s
                            """, (hintIdDb, session["id"],))
                
                flash(f"Je hebt {hintTitelDb} ontvangen, er zijn {hintWaardeDb} punten afgetrokken van je score", category="success")
                return redirect(url_for("hints.hints_mail"))
            
            # Laat de gebruiker weten dat hij/zij niet genoeg punten in bezit heeft
            flash("Je hebt niet genoeg punten om een hint te ontvangen", category="danger")
            return redirect(url_for("hints.hints_mail"))
        
        return render_template("hints/hints_mail.html", gebruikersnaam=session['name'], score=session['score'], results=table)
    
    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))


# --------------- socialmedia ---------------
@hints.route("/hints_socialmedia", methods=["POST", "GET"])
def hints_socialmedia():
     # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina  
    if 'loggedin' in session:
        # Haal de hint titel en beschrijving uit de database, dit wordt latenzien als je op de pagina komt
        cur.execute("""
                    select Hint.titel, Hint.beschrijving 
                    from Hint
                        inner join HintStatus on Hint.id = HintStatus.hintId
                    where Hint.hintPaginaId = 5 
                        and HintStatus.status = 1 
                        and HintStatus.gebruikerId = %s
                    """, (session["id"],)) 
        table = cur.fetchall()

        if request.method == "POST":
            # Haal de hintStatus, id, titel, gebruikerId en waarde uit de database
            cur.execute("""
                        select Hint.id, Hint.titel, Hint.waarde 
                        from Hint
                            inner join HintStatus on Hint.id = HintStatus.hintId
                        where Hint.hintPaginaId = 5
                            and HintStatus.status = 0 
                            and HintStatus.gebruikerId = %s
                        """, (session["id"],)) 
            data = cur.fetchone()

            # Alle hints zijn al ontvangen, geef dit door aan de gebruiker
            if data is None:
                flash("Je hebt alle hints al ontvangen", category="danger")
                return redirect(url_for("hints.hints_socialmedia"))

            # Zet database waardes in variabelen
            hintIdDb = data[0]
            hintTitelDb = data[1]
            hintWaardeDb = data[2]

            # Check of de gebruiker genoeg punten heeft, zo ja haal de hint waarde van de score af
            if session["score"] >= hintWaardeDb:
                # Score min hintwaarde
                session["score"] -= hintWaardeDb

                # Update de hintstatus in de database
                cur.execute("""
                            update HintStatus 
                            set status = 1 
                            where hintId = %s and gebruikerId = %s
                            """, (hintIdDb, session["id"],))
                
                flash(f"Je hebt {hintTitelDb} ontvangen, er zijn {hintWaardeDb} punten afgetrokken van je score", category="success")
                return redirect(url_for("hints.hints_socialmedia"))
            
            # Laat de gebruiker weten dat hij/zij niet genoeg punten in bezit heeft
            flash("Je hebt niet genoeg punten om een hint te ontvangen", category="danger")
            return redirect(url_for("hints.hints_socialmedia"))
        
        return render_template("hints/hints_socialmedia.html", gebruikersnaam=session['name'], score=session['score'], results=table)
    
    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))


# --------------- chatbot ---------------
@hints.route("/hints_chatbot", methods=["POST", "GET"])
def hints_chatbot():
    # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina  
    if 'loggedin' in session:
        # Haal de hint titel en beschrijving uit de database, dit wordt latenzien als je op de pagina komt
        cur.execute("""
                    select Hint.titel, Hint.beschrijving 
                    from Hint
                        inner join HintStatus on Hint.id = HintStatus.hintId
                    where Hint.hintPaginaId = 6 
                        and HintStatus.status = 1 
                        and HintStatus.gebruikerId = %s
                    """, (session["id"],)) 
        table = cur.fetchall()

        if request.method == "POST":
            # Haal de hintStatus, id, titel, gebruikerId en waarde uit de database
            cur.execute("""
                        select Hint.id, Hint.titel, Hint.waarde 
                        from Hint
                            inner join HintStatus on Hint.id = HintStatus.hintId
                        where Hint.hintPaginaId = 6
                            and HintStatus.status = 0 
                            and HintStatus.gebruikerId = %s
                        """, (session["id"],)) 
            data = cur.fetchone()

            # Alle hints zijn al ontvangen, geef dit door aan de gebruiker
            if data is None:
                flash("Je hebt alle hints al ontvangen", category="danger")
                return redirect(url_for("hints.hints_chatbot"))

            # Zet database waardes in variabelen
            hintIdDb = data[0]
            hintTitelDb = data[1]
            hintWaardeDb = data[2]

            # Check of de gebruiker genoeg punten heeft, zo ja haal de hint waarde van de score af
            if session["score"] >= hintWaardeDb:
                # Score min hintwaarde
                session["score"] -= hintWaardeDb

                # Update de hintstatus in de database
                cur.execute("""
                            update HintStatus 
                            set status = 1 
                            where hintId = %s and gebruikerId = %s
                            """, (hintIdDb, session["id"],))
                
                flash(f"Je hebt {hintTitelDb} ontvangen, er zijn {hintWaardeDb} punten afgetrokken van je score", category="success")
                return redirect(url_for("hints.hints_chatbot"))
            
            # Laat de gebruiker weten dat hij/zij niet genoeg punten in bezit heeft
            flash("Je hebt niet genoeg punten om een hint te ontvangen", category="danger")
            return redirect(url_for("hints.hints_chatbot"))
        
        return render_template("hints/hints_chatbot.html", gebruikersnaam=session['name'], score=session['score'], results=table)
    
    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))


# --------------- wireshark ---------------
@hints.route("/hints_wireshark", methods=["POST", "GET"])
def hints_wireshark():
    # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina  
    if 'loggedin' in session:
        # Haal de hint titel en beschrijving uit de database, dit wordt latenzien als je op de pagina komt
        cur.execute("""
                    select Hint.titel, Hint.beschrijving 
                    from Hint
                        inner join HintStatus on Hint.id = HintStatus.hintId
                    where Hint.hintPaginaId = 7 
                        and HintStatus.status = 1 
                        and HintStatus.gebruikerId = %s
                    """, (session["id"],)) 
        table = cur.fetchall()

        if request.method == "POST":
            # Haal de hintStatus, id, titel, gebruikerId en waarde uit de database
            cur.execute("""
                        select Hint.id, Hint.titel, Hint.waarde 
                        from Hint
                            inner join HintStatus on Hint.id = HintStatus.hintId
                        where Hint.hintPaginaId = 7
                            and HintStatus.status = 0 
                            and HintStatus.gebruikerId = %s
                        """, (session["id"],)) 
            data = cur.fetchone()

            # Alle hints zijn al ontvangen, geef dit door aan de gebruiker
            if data is None:
                flash("Je hebt alle hints al ontvangen", category="danger")
                return redirect(url_for("hints.hints_wireshark"))

            # Zet database waardes in variabelen
            hintIdDb = data[0]
            hintTitelDb = data[1]
            hintWaardeDb = data[2]

            # Check of de gebruiker genoeg punten heeft, zo ja haal de hint waarde van de score af
            if session["score"] >= hintWaardeDb:
                # Score min hintwaarde
                session["score"] -= hintWaardeDb

                # Update de hintstatus in de database
                cur.execute("""
                            update HintStatus 
                            set status = 1 
                            where hintId = %s and gebruikerId = %s
                            """, (hintIdDb, session["id"],))
                
                flash(f"Je hebt {hintTitelDb} ontvangen, er zijn {hintWaardeDb} punten afgetrokken van je score", category="success")
                return redirect(url_for("hints.hints_wireshark"))
            
            # Laat de gebruiker weten dat hij/zij niet genoeg punten in bezit heeft
            flash("Je hebt niet genoeg punten om een hint te ontvangen", category="danger")
            return redirect(url_for("hints.hints_wireshark"))
        
        return render_template("hints/hints_wireshark.html", gebruikersnaam=session['name'], score=session['score'], results=table)
    
    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))


# --------------- vlog ---------------
@hints.route("/hints_vlog", methods=["POST", "GET"])
def hints_vlog():
    # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina  
    if 'loggedin' in session:
        # Haal de hint titel en beschrijving uit de database, dit wordt latenzien als je op de pagina komt
        cur.execute("""
                    select Hint.titel, Hint.beschrijving 
                    from Hint
                        inner join HintStatus on Hint.id = HintStatus.hintId
                    where Hint.hintPaginaId = 8 
                        and HintStatus.status = 1 
                        and HintStatus.gebruikerId = %s
                    """, (session["id"],)) 
        table = cur.fetchall()

        if request.method == "POST":
            # Haal de hintStatus, id, titel, gebruikerId en waarde uit de database
            cur.execute("""
                        select Hint.id, Hint.titel, Hint.waarde 
                        from Hint
                            inner join HintStatus on Hint.id = HintStatus.hintId
                        where Hint.hintPaginaId = 8 
                            and HintStatus.status = 0 
                            and HintStatus.gebruikerId = %s
                        """, (session["id"],)) 
            data = cur.fetchone()

            # Alle hints zijn al ontvangen, geef dit door aan de gebruiker
            if data is None:
                flash("Je hebt alle hints al ontvangen", category="danger")
                return redirect(url_for("hints.hints_vlog"))

            # Zet database waardes in variabelen
            hintIdDb = data[0]
            hintTitelDb = data[1]
            hintWaardeDb = data[2]

            # Check of de gebruiker genoeg punten heeft, zo ja haal de hint waarde van de score af
            if session["score"] >= hintWaardeDb:
                # Score min hintwaarde
                session["score"] -= hintWaardeDb

                # Update de hintstatus in de database
                cur.execute("""
                            update HintStatus 
                            set status = 1 
                            where hintId = %s and gebruikerId = %s
                            """, (hintIdDb, session["id"],))
                
                flash(f"Je hebt {hintTitelDb} ontvangen, er zijn {hintWaardeDb} punten afgetrokken van je score", category="success")
                return redirect(url_for("hints.hints_vlog"))
            
            # Laat de gebruiker weten dat hij/zij niet genoeg punten in bezit heeft
            flash("Je hebt niet genoeg punten om een hint te ontvangen", category="danger")
            return redirect(url_for("hints.hints_vlog"))
        
        return render_template("hints/hints_vlog.html", gebruikersnaam=session['name'], score=session['score'], results=table)
    
    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))
