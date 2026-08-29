from flask import Blueprint, jsonify

from backend.app.service.desarrollo_service import obtener_informacion_desarrollo


desarrollo_router = Blueprint("desarrollo", __name__)


@desarrollo_router.route("/api/desarrollo")
def desarrollo():
    return jsonify(obtener_informacion_desarrollo())