from flask import Blueprint, render_template

from app.service.agricultura_service import obtener_informacion_agricultura


agricultura_router = Blueprint("agricultura", __name__)


@agricultura_router.route("/agricultura")
def agricultura():
    informacion = obtener_informacion_agricultura()

    return render_template(
        "agricultura.html",
        informacion=informacion
    )
