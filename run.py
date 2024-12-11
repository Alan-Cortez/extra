from flask import Flask
from apps.controllers.usuarios_controller import usuarios_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('instance.config')  # Si tienes configuraciones adicionales
    
    # Registrar blueprints
    app.register_blueprint(usuarios_bp, url_prefix='/usuarios')

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

