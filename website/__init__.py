from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'database.db'
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'azertyuiopqsdfghjklwxcvbn'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' 
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database successfully')


    