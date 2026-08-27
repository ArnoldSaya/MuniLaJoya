from flask import Blueprint, render_template

from app.service.saneamiento_service import obtener_informacion_saneamiento


saneamiento_router = Blueprint("saneamiento", __name__)


@saneamiento_router.route("/saneamiento")
def saneamiento():
    informacion = obtener_informacion_saneamiento()

    return render_template(
        "saneamiento.html",
        informacion=informacion
    )
