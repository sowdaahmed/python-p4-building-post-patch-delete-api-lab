from flask import Flask, request, jsonify, make_response
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return '<h1>Bakery API</h1>'

# GET all bakeries
@app.route('/bakeries', methods=['GET'])
def get_bakeries():
    bakeries = Bakery.query.all()
    return jsonify([b.to_dict() for b in bakeries]), 200

# GET baked goods
@app.route('/baked_goods', methods=['GET'])
def get_baked_goods():
    goods = BakedGood.query.all()
    return jsonify([g.to_dict() for g in goods]), 200

# ✅ POST a new baked good
@app.route('/baked_goods', methods=['POST'])
def create_baked_good():
    data = request.form
    new_good = BakedGood(
        name=data.get('name'),
        price=float(data.get('price')),
        bakery_id=int(data.get('bakery_id'))
    )
    db.session.add(new_good)
    db.session.commit()

    return jsonify(new_good.to_dict()), 201

# ✅ PATCH a bakery name
@app.route('/bakeries/<int:id>', methods=['PATCH'])
def update_bakery(id):
    bakery = Bakery.query.get_or_404(id)
    data = request.form

    if 'name' in data:
        bakery.name = data['name']

    db.session.commit()

    return jsonify(bakery.to_dict()), 200

# ✅ DELETE a baked good
@app.route('/baked_goods/<int:id>', methods=['DELETE'])
def delete_baked_good(id):
    baked_good = BakedGood.query.get_or_404(id)

    db.session.delete(baked_good)
    db.session.commit()

    return jsonify({"message": "Baked good deleted"}), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)
