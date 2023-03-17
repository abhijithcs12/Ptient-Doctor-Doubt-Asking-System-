from flask import Flask
from flask import *
from public import amal
from student import student
from teacher import teacher

app = Flask(__name__)

app.secret_key = "zion"

app.register_blueprint(amal)
app.register_blueprint(student,url_prefix="/student")
app.register_blueprint(teacher,url_prefix ="/teacher")
app.run(debug=True, port=5020)    