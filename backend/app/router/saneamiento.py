from flask import Blueprint, jsonify

from backend.app.service.saneamiento_service import obtener_informacion_saneamiento


saneamiento_router = Blueprint("saneamiento", __name__)


@saneamiento_router.route("/api/saneamiento")
def saneamiento():
    return jsonify(obtener_informacion_saneamiento())