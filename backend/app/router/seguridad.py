from flask import Blueprint, jsonify

from backend.app.service.seguridad_service import obtener_informacion_seguridad


seguridad_router = Blueprint("seguridad", __name__)


@seguridad_router.route("/api/seguridad")
def seguridad():
    return jsonify(obtener_informacion_seguridad())