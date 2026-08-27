from flask import Blueprint, render_template

from app.service.seguridad_service import obtener_informacion_seguridad


seguridad_router = Blueprint("seguridad", __name__)


@seguridad_router.route("/seguridad")
def seguridad():
    informacion = obtener_informacion_seguridad()

    return render_template(
        "seguridad.html",
        informacion=informacion
    )
