from flask import *
from public import *
from admin import *
from database import *


app=Flask(__name__)

app.register_blueprint(public)
app.register_blueprint(admin)

app.run(debug=True)