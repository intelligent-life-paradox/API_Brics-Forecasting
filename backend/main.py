from flask import Flask
from app.routes.predict import predict_bp
from config import Config

def create_app():
    """
    Inicializa a aplicação Flask com configuração e rotas registradas.
    """
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(predict_bp, url_prefix="/api")
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
