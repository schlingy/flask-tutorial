from flask import Flask
from dotenv import load_dotenv

def create_app():
    
    app = Flask(__name__)

    load_dotenv()

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app 