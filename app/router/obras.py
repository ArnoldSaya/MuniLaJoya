from flask import Blueprint, render_template

from app.service.obras_service import obtener_informacion_obras


obras_router = Blueprint("obras", __name__)


@obras_router.route("/obras")
def obras():
    informacion = obtener_informacion_obras()

    return render_template(
        "obras.html",
        informacion=informacion
    )
