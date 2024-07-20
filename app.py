from flask import Flask, render_template, request, jsonify
from models import db, connect_db, Cupcake


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'very secret'


connect_db(app)

@app.route('/')
def show_cupcakes():
    return render_template('/templates/index.html')