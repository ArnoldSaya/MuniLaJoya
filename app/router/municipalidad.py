from flask import Blueprint, render_template

from app.service.municipalidad_service import obtener_informacion_municipalidad


municipalidad_router = Blueprint("municipalidad", __name__)


@municipalidad_router.route("/municipalidad")
def municipalidad():
    informacion = obtener_informacion_municipalidad()

    return render_template(
        "municipalidad.html",
        informacion=informacion
    )
