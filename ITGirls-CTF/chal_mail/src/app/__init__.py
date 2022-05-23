from flask import Flask

app = Flask(__name__)
# app.config.from_object('config')
app.secret_key = "00d8d3f11739d2f3537099982b4674c29fc59a8fda350fca1379613adbb09119"
from app import routes