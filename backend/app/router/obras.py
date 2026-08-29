from flask import Blueprint, jsonify

from backend.app.service.obras_service import obtener_informacion_obras


obras_router = Blueprint("obras", __name__)


@obras_router.route("/api/obras")
def obras():
    return jsonify(obtener_informacion_obras())


@obras_router.route("/api/infraestructura")
def infraestructura():
    return jsonify(obtener_informacion_obras())