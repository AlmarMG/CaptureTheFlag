from flask import redirect, url_for, render_template, request, session, flash, Blueprint
import mariadb, sys, docker

stop_challenges = Blueprint('stop_challenges', __name__, template_folder='templates')

client = docker.from_env()

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


# --------------- stop pagina's ---------------
# --------------- moeilijk ---------------
@stop_challenges.route("/stop_moeilijk")
def stop_moeilijk():
    # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina
    if 'loggedin' in session:
        # Haal het id van de container op die gesloten moet worden
        id = containerId(f"chal-moeilijk_id-{session['id']}")

        # Er is geen container gevonden, geef dit door aan de gebruiker
        if id is None:
            flash('De challenge is nog niet gestart!', category='danger')
            return redirect(url_for('challenges'))
        
        # De container wordt verwijderd van de database
        cur.execute("""
                    delete from Container
                    where gebruikerId = %s and challengeNaam = 'moeilijk'
                    """, (session['id'],))

        # De container wordt geselecteerd
        container = client.containers.get(container_id=id)

        # De geselecteerde container wordt afgesloten
        container.stop(timeout=0)

        flash('Container succesvol afgesloten', category='success')
        return redirect(url_for('challenges'))

    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))


@stop_challenges.route("/stop_vlog")
def stop_vlog():
   # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina
    if 'loggedin' in session:
        # Haal het id van de container op die gesloten moet worden
        id = containerId(f"chal-vlog_id-{session['id']}")

        # Er is geen container gevonden, geef dit door aan de gebruiker
        if id is None:
            flash('De challenge is nog niet gestart!', category='danger')
            return redirect(url_for('challenges'))
        
        # De container wordt verwijderd van de database
        cur.execute("""
                    delete from Container
                    where gebruikerId = %s and challengeNaam = 'vlog'
                    """, (session['id'],))

        # De container wordt geselecteerd
        container = client.containers.get(container_id=id)

        # De geselecteerde container wordt afgesloten
        container.stop(timeout=0)

        flash('Container succesvol afgesloten', category='success')
        return redirect(url_for('challenges'))

    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))


@stop_challenges.route("/stop_chatbot")
def stop_chatbot():
    # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina
    if 'loggedin' in session:
        # Haal het id van de container op die gesloten moet worden
        id = containerId(f"chal-chatbot_id-{session['id']}")

        # Er is geen container gevonden, geef dit door aan de gebruiker
        if id is None:
            flash('De challenge is nog niet gestart!', category='danger')
            return redirect(url_for('challenges'))
        
        # De container wordt verwijderd van de database
        cur.execute("""
                    delete from Container
                    where gebruikerId = %s and challengeNaam = 'chatbot'
                    """, (session['id'],))

        # De container wordt geselecteerd
        container = client.containers.get(container_id=id)

        # De geselecteerde container wordt afgesloten
        container.stop(timeout=0)

        flash('Container succesvol afgesloten', category='success')
        return redirect(url_for('challenges'))

    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))



@stop_challenges.route("/stop_mail")
def stop_mail():
    # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina
    if 'loggedin' in session:
        # Haal het id van de container op die gesloten moet worden
        id = containerId(f"chal-mail_id-{session['id']}")

        # Er is geen container gevonden, geef dit door aan de gebruiker
        if id is None:
            flash('De challenge is nog niet gestart!', category='danger')
            return redirect(url_for('challenges'))
        
        # De container wordt verwijderd van de database
        cur.execute("""
                    delete from Container
                    where gebruikerId = %s and challengeNaam = 'mail'
                    """, (session['id'],))

        # De container wordt geselecteerd
        container = client.containers.get(container_id=id)

        # De geselecteerde container wordt afgesloten
        container.stop(timeout=0)

        flash('Container succesvol afgesloten', category='success')
        return redirect(url_for('challenges'))

    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))


@stop_challenges.route("/stop_socialmedia")
def stop_socialmedia():
    # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina
    if 'loggedin' in session:
        # Haal het id van de container op die gesloten moet worden
        id = containerId(f"chal-socialmedia_id-{session['id']}")

        # Er is geen container gevonden, geef dit door aan de gebruiker
        if id is None:
            flash('De challenge is nog niet gestart!', category='danger')
            return redirect(url_for('challenges'))
        
        # De container wordt verwijderd van de database
        cur.execute("""
                    delete from Container
                    where gebruikerId = %s and challengeNaam = 'socialmedia'
                    """, (session['id'],))

        # De container wordt geselecteerd
        container = client.containers.get(container_id=id)

        # De geselecteerde container wordt afgesloten
        container.stop(timeout=0)

        flash('Container succesvol afgesloten', category='success')
        return redirect(url_for('challenges'))

    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))


@stop_challenges.route("/stop_wireshark")
def stop_wireshark():
    # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina
    if 'loggedin' in session:
        # Haal het id van de container op die gesloten moet worden
        id = containerId(f"chal-wireshark_id-{session['id']}")

        # Er is geen container gevonden, geef dit door aan de gebruiker
        if id is None:
            flash('De challenge is nog niet gestart!', category='danger')
            return redirect(url_for('challenges'))
        
        # De container wordt verwijderd van de database
        cur.execute("""
                    delete from Container
                    where gebruikerId = %s and challengeNaam = 'wireshark'
                    """, (session['id'],))

        # De container wordt geselecteerd
        container = client.containers.get(container_id=id)

        # De geselecteerde container wordt afgesloten
        container.stop(timeout=0)

        flash('Container succesvol afgesloten', category='success')
        return redirect(url_for('challenges'))

    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))


@stop_challenges.route("/stop_encodedchat")
def stop_encodedchat():
    # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina
    if 'loggedin' in session:
        # Haal het id van de container op die gesloten moet worden
        id = containerId(f"chal-encodedchat_id-{session['id']}")

        # Er is geen container gevonden, geef dit door aan de gebruiker
        if id is None:
            flash('De challenge is nog niet gestart!', category='danger')
            return redirect(url_for('challenges'))
        
        # De container wordt verwijderd van de database
        cur.execute("""
                    delete from Container
                    where gebruikerId = %s and challengeNaam = 'encodedchat'
                    """, (session['id'],))

        # De container wordt geselecteerd
        container = client.containers.get(container_id=id)

        # De geselecteerde container wordt afgesloten
        container.stop(timeout=0)

        flash('Container succesvol afgesloten', category='success')
        return redirect(url_for('challenges'))

    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))


@stop_challenges.route("/stop_cookie")
def stop_cookie():
    # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina
    if 'loggedin' in session:
        # Haal het id van de container op die gesloten moet worden
        id = containerId(f"chal-cookie_id-{session['id']}")

        # Er is geen container gevonden, geef dit door aan de gebruiker
        if id is None:
            flash('De challenge is nog niet gestart!', category='danger')
            return redirect(url_for('challenges'))
        
        # De container wordt verwijderd van de database
        cur.execute("""
                    delete from Container
                    where gebruikerId = %s and challengeNaam = 'cookie'
                    """, (session['id'],))

        # De container wordt geselecteerd
        container = client.containers.get(container_id=id)

        # De geselecteerde container wordt afgesloten
        container.stop(timeout=0)

        flash('Container succesvol afgesloten', category='success')
        return redirect(url_for('challenges'))

    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))
