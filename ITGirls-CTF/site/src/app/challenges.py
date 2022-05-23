from flask import redirect, url_for, render_template, request, session, flash, Blueprint
import time, mariadb, docker, sys

# Blueprint aanmaken
challenges = Blueprint('challenges', __name__, template_folder='templates')


# Docker initializeren
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


# --------------- challenges starten ---------------
# --------------- vlog ---------------
@challenges.route("/vlog")
def vlog():
    # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina  
    if 'loggedin' in session:
        # Haal de status van de container uit de database
        cur.execute("""
                    select status, port 
                    from Container 
                    where challengeNaam = 'vlog' and gebruikerId = %s
                    """, (session['id'],))
        container = cur.fetchone()
        # Check of de gebruiker al een container open heeft staan, zo ja verbind door naar de container
        if container is not None:
            usedPort = container[1]
            return redirect(f'http://vlog.localhost:{usedPort}/', code=301)

        # Haal de hoogste en laagste port uit de database
        cur.execute("""
                    Select MIN(port) as min,
                    MAX(port) as max
                    from Container where challengeNaam = 'vlog'
                    """)
        minPort, maxPort = cur.fetchone()

        # Definieer laagste port van challenge
        basePort = 8000

        # check of de gebruiker de eerste is die een container start, check dan of de min port groter is dan de basePort anders wordt de port += 1
        if minPort is None:
            port = basePort
        elif minPort > basePort:
            port  = minPort - 1
        else:
            maxPort = int(maxPort)
            port =  maxPort + 1

        # Zet container informatie in de database
        cur.execute("""
                    insert into Container (gebruikerId, challengeNaam, port, status) 
                    values (%s, 'vlog', %s, 1)
                    """, (session['id'], port,))

        # Start de container
        client.containers.run("chal_vlog", extra_hosts={"vlog.localhost":"127.0.0.1"}, 
                            name=f"chal-vlog_id-{session['id']}", ports={'80/tcp': port}, 
                            auto_remove=True, detach=True)

        # Wacht 1 seconde zodat alles goed opstart
        time.sleep(1)
        return redirect(f'http://vlog.localhost:{port}/', code=301)
    
    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))


# --------------- moeilijk ---------------
@challenges.route("/moeilijk")
def moeilijk():
    # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina  
    if 'loggedin' in session:
        # Haal de status van de container uit de database
        cur.execute("""
                    select status, port 
                    from Container 
                    where challengeNaam = 'moeilijk' and gebruikerId = %s
                    """, (session['id'],))
        container = cur.fetchone()
        # Check of de gebruiker al een container open heeft staan, zo ja verbind door naar de container
        if container is not None:
            usedPort = container[1]
            return redirect(f'http://moeilijk.localhost:{usedPort}/', code=301)

        # Haal de hoogste en laagste port uit de database
        cur.execute("""
                    Select MIN(port) as min,
                    MAX(port) as max
                    from Container where challengeNaam = 'moeilijk'
                    """)
        minPort, maxPort = cur.fetchone()

        # Definieer laagste port van challenge
        basePort = 8100

        # check of de gebruiker de eerste is die een container start, check dan of de min port groter is dan de basePort anders wordt de port += 1
        if minPort is None:
            port = basePort
        elif minPort > basePort:
            port  = minPort - 1
        else:
            maxPort = int(maxPort)
            port =  maxPort + 1

        # Zet container informatie in de database
        cur.execute("""
                    insert into Container (gebruikerId, challengeNaam, port, status) 
                    values (%s, 'moeilijk', %s, 1)
                    """, (session['id'], port,))

        # Start de container
        client.containers.run("chal_moeilijk", extra_hosts={"moeilijk.localhost":"127.0.0.1"}, 
                            name=f"chal-moeilijk_id-{session['id']}", ports={'80/tcp': port}, 
                            auto_remove=True, detach=True)

        # Wacht 1 seconde zodat alles goed opstart
        time.sleep(1)
        return redirect(f'http://moeilijk.localhost:{port}/', code=301)
    
    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))


# --------------- wireshark ---------------
@challenges.route("/wireshark")
def wireshark():
    # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina  
    if 'loggedin' in session:
        # Haal de status van de container uit de database
        cur.execute("""
                    select status, port 
                    from Container 
                    where challengeNaam = 'wireshark' and gebruikerId = %s
                    """, (session['id'],))
        container = cur.fetchone()
        # Check of de gebruiker al een container open heeft staan, zo ja verbind door naar de container
        if container is not None:
            usedPort = container[1]
            return redirect(f'http://wireshark.localhost:{usedPort}/', code=301)

        # Haal de hoogste en laagste port uit de database
        cur.execute("""
                    Select MIN(port) as min,
                    MAX(port) as max
                    from Container where challengeNaam = 'wireshark'
                    """)
        minPort, maxPort = cur.fetchone()

        # Definieer laagste port van challenge
        basePort = 8200

        # check of de gebruiker de eerste is die een container start, check dan of de min port groter is dan de basePort anders wordt de port += 1
        if minPort is None:
            port = basePort
        elif minPort > basePort:
            port  = minPort - 1
        else:
            maxPort = int(maxPort)
            port =  maxPort + 1

        # Zet container informatie in de database
        cur.execute("""
                    insert into Container (gebruikerId, challengeNaam, port, status) 
                    values (%s, 'wireshark', %s, 1)
                    """, (session['id'], port,))

        # Start de container
        client.containers.run("chal_wireshark", extra_hosts={"wireshark.localhost":"127.0.0.1"}, 
                            name=f"chal-wireshark_id-{session['id']}", ports={'80/tcp': port}, 
                            auto_remove=True, detach=True)

        # Wacht 1 seconde zodat alles goed opstart
        time.sleep(1)
        return redirect(f'http://wireshark.localhost:{port}/', code=301)
    
    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))


# --------------- encodedchat ---------------
@challenges.route("/encodedchat")
def encodedchat():
 # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina  
    if 'loggedin' in session:
        # Haal de status van de container uit de database
        cur.execute("""
                    select status, port 
                    from Container 
                    where challengeNaam = 'encodedchat' and gebruikerId = %s
                    """, (session['id'],))
        container = cur.fetchone()
        # Check of de gebruiker al een container open heeft staan, zo ja verbind door naar de container
        if container is not None:
            usedPort = container[1]
            return redirect(f'http://encodedchat.localhost:{usedPort}/', code=301)

        # Haal de hoogste en laagste port uit de database
        cur.execute("""
                    Select MIN(port) as min,
                    MAX(port) as max
                    from Container where challengeNaam = 'encodedchat'
                    """)
        minPort, maxPort = cur.fetchone()

        # Definieer laagste port van challenge
        basePort = 8300

        # check of de gebruiker de eerste is die een container start, check dan of de min port groter is dan de basePort anders wordt de port += 1
        if minPort is None:
            port = basePort
        elif minPort > basePort:
            port  = minPort - 1
        else:
            maxPort = int(maxPort)
            port =  maxPort + 1

        # Zet container informatie in de database
        cur.execute("""
                    insert into Container (gebruikerId, challengeNaam, port, status) 
                    values (%s, 'encodedchat', %s, 1)
                    """, (session['id'], port,))

        # Start de container
        client.containers.run("chal_encodedchat", extra_hosts={"encodedchat.localhost":"127.0.0.1"}, 
                            name=f"chal-encodedchat_id-{session['id']}", ports={'80/tcp': port}, 
                            auto_remove=True, detach=True)

        # Wacht 1 seconde zodat alles goed opstart
        time.sleep(1)
        return redirect(f'http://encodedchat.localhost:{port}/', code=301)
    
    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))


# --------------- cookie ---------------
@challenges.route("/cookie")
def cookie():
    # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina  
    if 'loggedin' in session:
        # Haal de status van de container uit de database
        cur.execute("""
                    select status, port 
                    from Container 
                    where challengeNaam = 'cookie' and gebruikerId = %s
                    """, (session['id'],))
        container = cur.fetchone()
        # Check of de gebruiker al een container open heeft staan, zo ja verbind door naar de container
        if container is not None:
            usedPort = container[1]
            return redirect(f'http://cookie.localhost:{usedPort}/', code=301)

        # Haal de hoogste en laagste port uit de database
        cur.execute("""
                    Select MIN(port) as min,
                    MAX(port) as max
                    from Container where challengeNaam = 'cookie'
                    """)
        minPort, maxPort = cur.fetchone()

        # Definieer laagste port van challenge
        basePort = 8400

        # check of de gebruiker de eerste is die een container start, check dan of de min port groter is dan de basePort anders wordt de port += 1
        if minPort is None:
            port = basePort
        elif minPort > basePort:
            port  = minPort - 1
        else:
            maxPort = int(maxPort)
            port =  maxPort + 1

        # Zet container informatie in de database
        cur.execute("""
                    insert into Container (gebruikerId, challengeNaam, port, status) 
                    values (%s, 'cookie', %s, 1)
                    """, (session['id'], port,))

        # Start de container
        client.containers.run("chal_cookie", extra_hosts={"cookie.localhost":"127.0.0.1"}, 
                            name=f"chal-cookie_id-{session['id']}", ports={'80/tcp': port}, 
                            auto_remove=True, detach=True)

        # Wacht 1 seconde zodat alles goed opstart
        time.sleep(1)
        return redirect(f'http://cookie.localhost:{port}/', code=301)
    
    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))


# --------------- mail ---------------
@challenges.route("/mail")
def mail():
     # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina  
    if 'loggedin' in session:
        # Haal de status van de container uit de database
        cur.execute("""
                    select status, port 
                    from Container 
                    where challengeNaam = 'mail' and gebruikerId = %s
                    """, (session['id'],))
        container = cur.fetchone()
        # Check of de gebruiker al een container open heeft staan, zo ja verbind door naar de container
        if container is not None:
            usedPort = container[1]
            return redirect(f'http://mail.localhost:{usedPort}/', code=301)

        # Haal de hoogste en laagste port uit de database
        cur.execute("""
                    Select MIN(port) as min,
                    MAX(port) as max
                    from Container where challengeNaam = 'mail'
                    """)
        minPort, maxPort = cur.fetchone()

        # Definieer laagste port van challenge
        basePort = 8500

        # check of de gebruiker de eerste is die een container start, check dan of de min port groter is dan de basePort anders wordt de port += 1
        if minPort is None:
            port = basePort
        elif minPort > basePort:
            port  = minPort - 1
        else:
            maxPort = int(maxPort)
            port =  maxPort + 1

        # Zet container informatie in de database
        cur.execute("""
                    insert into Container (gebruikerId, challengeNaam, port, status) 
                    values (%s, 'mail', %s, 1)
                    """, (session['id'], port,))

        # Start de container
        client.containers.run("chal_mail", extra_hosts={"mail.localhost":"127.0.0.1"}, 
                            name=f"chal-mail_id-{session['id']}", ports={'80/tcp': port}, 
                            auto_remove=True, detach=True)

        # Wacht 1 seconde zodat alles goed opstart
        time.sleep(1)
        return redirect(f'http://mail.localhost:{port}/', code=301)
    
    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))


# --------------- socialmedia ---------------
@challenges.route("/socialmedia")
def socialmedia():
     # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina  
    if 'loggedin' in session:
        # Haal de status van de container uit de database
        cur.execute("""
                    select status, port 
                    from Container 
                    where challengeNaam = 'socialmedia' and gebruikerId = %s
                    """, (session['id'],))
        container = cur.fetchone()
        # Check of de gebruiker al een container open heeft staan, zo ja verbind door naar de container
        if container is not None:
            usedPort = container[1]
            return redirect(f'http://socialmedia.localhost:{usedPort}/', code=301)

        # Haal de hoogste en laagste port uit de database
        cur.execute("""
                    Select MIN(port) as min,
                    MAX(port) as max
                    from Container where challengeNaam = 'socialmedia'
                    """)
        minPort, maxPort = cur.fetchone()

        # Definieer laagste port van challenge
        basePort = 8600

        # check of de gebruiker de eerste is die een container start, check dan of de min port groter is dan de basePort anders wordt de port += 1
        if minPort is None:
            port = basePort
        elif minPort > basePort:
            port  = minPort - 1
        else:
            maxPort = int(maxPort)
            port =  maxPort + 1

        # Zet container informatie in de database
        cur.execute("""
                    insert into Container (gebruikerId, challengeNaam, port, status) 
                    values (%s, 'socialmedia', %s, 1)
                    """, (session['id'], port,))

        # Start de container
        client.containers.run("chal_socialmedia", extra_hosts={"socialmedia.localhost":"127.0.0.1"}, 
                            name=f"chal-socialmedia_id-{session['id']}", ports={'80/tcp': port}, 
                            auto_remove=True, detach=True)

        # Wacht 1 seconde zodat alles goed opstart
        time.sleep(1)
        return redirect(f'http://socialmedia.localhost:{port}/', code=301)
    
    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))


# --------------- chatbot ---------------
@challenges.route("/chatbot")
def chatbot():
     # Check of de gebruiker al is ingelogd, zo nee, verbind door naar login pagina  
    if 'loggedin' in session:
        # Haal de status van de container uit de database
        cur.execute("""
                    select status, port 
                    from Container 
                    where challengeNaam = 'chatbot' and gebruikerId = %s
                    """, (session['id'],))
        container = cur.fetchone()
        # Check of de gebruiker al een container open heeft staan, zo ja verbind door naar de container
        if container is not None:
            usedPort = container[1]
            return redirect(f'http://chatbot.localhost:{usedPort}/', code=301)

        # Haal de hoogste en laagste port uit de database
        cur.execute("""
                    Select MIN(port) as min,
                    MAX(port) as max
                    from Container where challengeNaam = 'chatbot'
                    """)
        minPort, maxPort = cur.fetchone()

        # Definieer laagste port van challenge
        basePort = 8700

        # check of de gebruiker de eerste is die een container start, check dan of de min port groter is dan de basePort anders wordt de port += 1
        if minPort is None:
            port = basePort
        elif minPort > basePort:
            port  = minPort - 1
        else:
            maxPort = int(maxPort)
            port =  maxPort + 1

        # Zet container informatie in de database
        cur.execute("""
                    insert into Container (gebruikerId, challengeNaam, port, status) 
                    values (%s, 'chatbot', %s, 1)
                    """, (session['id'], port,))

        # Start de container
        client.containers.run("chal_chatbot", extra_hosts={"chatbot.localhost":"127.0.0.1"}, 
                            name=f"chal-chatbot_id-{session['id']}", ports={'80/tcp': port}, 
                            auto_remove=True, detach=True)

        # Wacht 1 seconde zodat alles goed opstart
        time.sleep(1)
        return redirect(f'http://chatbot.localhost:{port}/', code=301)
    
    flash("Inloggen is verplicht!", category="danger")
    return redirect(url_for('login'))
