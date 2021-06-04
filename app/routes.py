from app import db
from app.models.planet import Planet
from flask import request, Blueprint, make_response, jsonify

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planet_bp.route("", methods=["GET"])
def handle_planets():
    planets = Planet.query.all()
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "has_rings": planet.has_rings
        })
        return jsonify(planets_response)
