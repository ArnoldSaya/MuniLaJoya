from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    CORS(app)

    from backend.app.router.home import home_router
    from backend.app.router.municipalidad import municipalidad_router
    from backend.app.router.saneamiento import saneamiento_router
    from backend.app.router.seguridad import seguridad_router
    from backend.app.router.desarrollo import desarrollo_router
    from backend.app.router.obras import obras_router
    from backend.app.router.agricultura import agricultura_router

    app.register_blueprint(home_router)
    app.register_blueprint(municipalidad_router)
    app.register_blueprint(saneamiento_router)
    app.register_blueprint(seguridad_router)
    app.register_blueprint(desarrollo_router)
    app.register_blueprint(obras_router)
    app.register_blueprint(agricultura_router)

    return app
