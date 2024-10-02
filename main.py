from flask import *
from public import *

app=Flask(__name__)

app.register_blueprint(public)

app.run(debug=True)