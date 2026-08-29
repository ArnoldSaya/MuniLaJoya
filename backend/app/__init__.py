from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    CORS(app)

    from app.router.home import home_router
    from app.router.municipalidad import municipalidad_router
    from app.router.saneamiento import saneamiento_router
    from app.router.seguridad import seguridad_router
    from app.router.desarrollo import desarrollo_router
    from app.router.obras import obras_router
    from app.router.agricultura import agricultura_router

    app.register_blueprint(home_router)
    app.register_blueprint(municipalidad_router)
    app.register_blueprint(saneamiento_router)
    app.register_blueprint(seguridad_router)
    app.register_blueprint(desarrollo_router)
    app.register_blueprint(obras_router)
    app.register_blueprint(agricultura_router)

    return app
