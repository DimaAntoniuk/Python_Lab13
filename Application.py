from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from Main import main

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://newuser:newuser@localhost:3306/exhibit_db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class ExhibitModel(db.Model):
    __tablename__ = 'exhibits'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=80))
    century_of_creation = db.Column(db.Integer)
    country_of_creation = db.Column(db.String(length=80))
    size = db.Column(db.Integer)
    destroyed_in_persentage = db.Column(db.Integer)

    def __init__(self, name = "", century_of_creation = 0,
            country_of_creation = "", size = 0, destroyed_in_persentage = 0):
        self.name = name
        self.century_of_creation = century_of_creation
        self.country_of_creation = country_of_creation
        self.size = size
        self.destroyed_in_persentage = destroyed_in_persentage

    def __str__(self):
        return "{" + "name='" + str(self.name) + '\'' \
               + ", century_of_creation='" + str(self.century_of_creation) + '\'' \
               + ", country_of_creation=" + str(self.country_of_creation) \
               + ", size=" + str(self.size) \
               + ", destroyed_in_persentage=" + str(self.destroyed_in_persentage) + "}"

class ExhibitSchema(ma.Schema):
    class Meta:
        fields = ('name', 'century_of_creation', 'country_of_creation', 'size',
                'destroyed_in_persentage')

exhibit_schema = ExhibitSchema()
exhibits_schema = ExhibitSchema(many=True)
db.create_all()

@app.route("/exhibitspy", methods=["POST"])
def add_exhibit():
    name = request.get_json()["name"]
    century_of_creation = request.get_json()["century_of_creation"]
    country_of_creation = request.get_json()["country_of_creation"]
    size = request.get_json()["size"]
    destroyed_in_persentage = request.get_json()['destroyed_in_persentage']
    new_exhibit = ExhibitModel(name, century_of_creation,
            country_of_creation, size, destroyed_in_persentage)
    db.session.add(new_exhibit)
    db.session.commit()
    return jsonify(request.json)

@app.route("/exhibitspy", methods=["GET"])
def get_exhibits():
    all_exhibits = ExhibitModel.query.all()
    return_info = exhibits_schema.dump(all_exhibits)
    return jsonify(return_info.data)

@app.route("/exhibitspy/<id>", methods=["GET"])
def get_exhibit_by_id(id):
    exhibit = ExhibitModel.query.get(id)
    return exhibit_schema.jsonify(exhibit)

@app.route("/exhibitspy/<id>", methods=["PUT"])
def replace_exhibit(id):
    exhibit = ExhibitModel.query.get(id)
    exhibit.name = request.json["name"]
    exhibit.century_of_creation = request.json["century_of_creation"]
    exhibit.country_of_creation = request.json["country_of_creation"]
    exhibit.size = request.json["size"]
    exhibit.destroyed_in_persentage = request.json["destroyed_in_persentage"]
    db.session.commit()
    return exhibit_schema.jsonify(request.json)


@app.route("/exhibitspy/<id>", methods=["DELETE"])
def delete_exhibit(id):
    exhibit = ExhibitModel.query.get(id)
    db.session.delete(exhibit)
    db.session.commit()
    return exhibit_schema.jsonify(exhibit)

if __name__ == '__main__':
    app.run()
