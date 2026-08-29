from flask import Blueprint, jsonify

home_router = Blueprint("home", __name__)


@home_router.route("/api/home")
def home():
    return jsonify(
        {
            "titulo": "Inicio",
            "descripcion": "Bienvenido a la Municipalidad de La Joya.",
        }
    )