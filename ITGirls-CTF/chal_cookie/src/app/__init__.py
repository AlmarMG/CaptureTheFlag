from flask import Flask

app = Flask(__name__)
app.secret_key = "d7e83e28a04b537e64424546b14caf9b67bad2f28dabce68116e0d372319fa00"

from app import routes