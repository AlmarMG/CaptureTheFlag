from flask import Flask

app = Flask(__name__)
app.secret_key = "f462a4eb1b8a8819823a7fc1fe78e88ea987456e84f38a20909b9ed21f51dfd2"

from app import routes