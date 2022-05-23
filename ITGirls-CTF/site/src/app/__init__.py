from flask import Flask
from app.challenges import challenges
from app.hints import hints
from app.stop_challenges import stop_challenges
 
app = Flask(__name__)

app.secret_key = "e5c6d5d6f0f81c762208063594842e9a068580299997dfd96f624469c4b7bc17"
app.register_blueprint(challenges)
app.register_blueprint(hints)
app.register_blueprint(stop_challenges)

from app import routes
from app import error_pages