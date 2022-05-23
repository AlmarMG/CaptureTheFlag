from flask import Flask

app = Flask(__name__)
app.secret_key = "1Z9v3gQJzacjITHHPkx1xIFij6aNs1Npu4bM235rD9a42WTBu4FIDF40oBjMfNMh"

from app import routes