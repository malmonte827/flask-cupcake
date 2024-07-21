from flask import Flask, render_template, request, jsonify
from models import db, connect_db, Cupcake


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///cupcakes_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'very secret'


connect_db(app)

@app.route('/')
def homepage():
    return render_template('/index.html')

@app.route('/api/cupcakes', methods=['GET'])
def list_cupcakes():
    """ Shows all cupcakes """

    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]

    return  jsonify(cupcakes=cupcakes)


@app.route('/api/cupcakes/<int:id>', methods=['GET'])
def show_cupcake(id):
    """ Display details on a specific cupcake """

    cupcake = Cupcake.query.get_or_404(id)

    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    """ Adds new cupcake """

    data = request.json

    cupcake = Cupcake(
        flavor=data['flavor'],
        size=data['size'],
        rating=data['rating'],
        image=data['image'] or None
    )

    db.session.add(cupcake)
    db.session.commit()

    return (jsonify(cupcake=cupcake.serialize()), 201)

@app.route('/api/cupcake/<int:id>')
def update_cupcake():
    """ updates existing cupcake """

    cupcake = Cupcake.query.get_or_404(id)
    data = request.json

    cupcake.flavor=data['flavor']
    cupcake.size=data['size']
    cupcake.rating=data['rating']
    cupcake.image=data['image']

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.serialize() )

@app.route('/api/cupcake/<int:id>')
def delete_cupcake(id):
    """ delete existing cupcake """

    cupcake = Cupcake.query.get_or_404(id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message='deleted')
