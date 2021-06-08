from app import db
from app.models.planet import Planet
from flask import request, Blueprint, make_response, jsonify

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planet_bp.route("/", methods=["GET", "POST"])
def handle_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "has_rings": planet.has_rings
            })
        return make_response(jsonify(planets_response), 200)
        # return jsonify(planets_response), 200
    elif request.method == 'POST':
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
                            description=request_body["description"], has_rings=request_body["has_rings"])
        db.session.add(new_planet)
        db.session.commit()
        return make_response(f"Planet {new_planet.name} successfully created", 201)


@ planet_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if not planet:
        return make_response(f"Planet {planet_id} not found", 404)

    if request.method == "GET":

        planets_response = [{
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "has_rings": planet.has_rings
        }]
        return make_response(jsonify(planets_response), 200)
    elif request.method == "PUT":
        form_data = request.get_json()
        planet.name = form_data["name"]
        planet.description = form_data["description"]
        planet.has_rings = form_data["has_rings"]

        db.session.commit()

        return make_response(f"Planet {planet.name} successfully updated", 200)

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()

        return make_response(f"Planet {planet.name} successfully deleted", 200)
