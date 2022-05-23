from flask import Flask

app = Flask(__name__)
app.secret_key = "f1797f6cfbc94e6e59183987140b720dae12ddb11de57b372e1406d23388927c"

from app import routes