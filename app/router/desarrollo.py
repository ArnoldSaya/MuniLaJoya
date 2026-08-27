from flask import Blueprint, render_template

from app.service.desarrollo_service import obtener_informacion_desarrollo


desarrollo_router = Blueprint("desarrollo", __name__)


@desarrollo_router.route("/desarrollo")
def desarrollo():
    informacion = obtener_informacion_desarrollo()

    return render_template(
        "desarrollo.html",
        informacion=informacion
    )
