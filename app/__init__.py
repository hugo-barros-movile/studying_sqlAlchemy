from flask import Flask
from app.controllers.main import main
from app.models import db


def create_app(object_name, env="dev"):

    app = Flask(__name__)

    # Config coming from app.settings.%sConfig
    app.config.from_object(object_name)
    app.config['ENV'] = env


    db.init_app(app)
    with app.app_context():
    	db.create_all()
    	
    app.register_blueprint(main)

    return app
