from flask import Blueprint, jsonify

from app.service.agricultura_service import obtener_informacion_agricultura


agricultura_router = Blueprint("agricultura", __name__)


@agricultura_router.route("/api/agricultura")
def agricultura():
    return jsonify(obtener_informacion_agricultura())