from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Plant

app = Flask(__name__)

# Database config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

# Initialize database
db.init_app(app)
migrate = Migrate(app, db)


# --------------------
# ROUTES
# --------------------

# GET /plants
@app.route("/plants", methods=["GET"])
def get_plants():
    plants = Plant.query.all()
    return jsonify([plant.to_dict() for plant in plants]), 200


# GET /plants/<id>
@app.route("/plants/<int:id>", methods=["GET"])
def get_plant(id):
    plant = db.session.get(Plant, id)

    if not plant:
        return {"error": "Plant not found"}, 404

    return plant.to_dict(), 200


# POST /plants
@app.route("/plants", methods=["POST"])
def create_plant():
    data = request.get_json()

    plant = Plant(
        name=data["name"],
        image=data["image"],
        price=data["price"]
    )

    db.session.add(plant)
    db.session.commit()

    return plant.to_dict(), 201


# --------------------
# RUN APP
# --------------------
if __name__ == "__main__":
    app.run(port=5555, debug=True)
