from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_cors import CORS
import os
#from pymongo.mongo_client import MongoClient
#from pymongo.server_api import ServerApi
# from flask_pymongo import PyMongo

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r'/*': {"origins": "*"}}, headers='Content-Type')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    
    app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get('Elephant')
    
    from app.models.host import Host
    from app.models.home import Home
    from app.models.towel import Towel
    from app.models.trash import Trash
    from app.models.item import Item


    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    
    from app.routes.home_routes import home_bp
    from app.routes.host_routes import host_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(host_bp)

    CORS(app)
    return app
