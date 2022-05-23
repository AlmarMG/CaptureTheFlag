from flask import render_template, request
from flask_mail import Mail, Message
from app import app

# Mail configureren
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "itgirlsctf123@gmail.com"
app.config['MAIL_PASSWORD'] = "ITGirls.ctf12345"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# Mail initializeren
mail = Mail(app)


# --------------- error 404, Not found pagina ---------------
@app.errorhandler(404)
def not_found(e):

    # Nieuwe email aanmaken met error
    email = "itgirlsctf123@gmail.com"
    subject = "404 error"
    msg = f"Server error: {e}, route: {request.url}"

    # Nieuwe mail verzenden naar itgirls mail
    message = Message(subject=subject, sender="itgirlsctf123@gmail.com", recipients=[email], body=msg)
    mail.send(message)

    return render_template("error_pages/404.html")


# --------------- error 500, Server error pagina ---------------
@app.errorhandler(500)
def server_error(e):

    # Nieuwe email aanmaken met error
    email = "itgirlsctf123@gmail.com"
    subject = "500 error"
    msg = f"Server error: {e}, route: {request.url}"

    # Nieuwe mail verzenden naar itgirls mail
    message = Message(subject=subject, sender="itgirlsctf123@gmail.com", recipients=[email], body=msg)
    mail.send(message)

    return render_template("error_pages/500.html")

