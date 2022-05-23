from flask import Flask

app = Flask(__name__)
app.secret_key = "185f336db632e083a16e5536c2a7224f05b717e1aa630c7158494e24db221768"

from app import routes