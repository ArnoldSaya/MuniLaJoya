from flask import Blueprint, jsonify

from backend.app.service.municipalidad_service import obtener_informacion_municipalidad


municipalidad_router = Blueprint("municipalidad", __name__)


@municipalidad_router.route("/api/municipalidad")
def municipalidad():
    return jsonify(obtener_informacion_municipalidad())