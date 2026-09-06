from flask import Flask
from app.routes.productos import productos_bp
from app.routes.auth import auth_bp
from app.routes.ventas import ventas_bp

def create_app():
    
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "API EzePC funcionando"

    # Registramos los blueprints

    # Registramos los productos
    app.register_blueprint(productos_bp)

    # Registramos la autenticación
    app.register_blueprint(auth_bp)

    # Registramos las ventas
    app.register_blueprint(ventas_bp)

    return app