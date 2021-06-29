from www.views import transactions
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_login import UserMixin
from sqlalchemy.sql import func

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app(): 
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Cobra Commander is not awesome'
    
    app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///DB/{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .transactions import transactions
  
    

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(transactions, url_prefix='/')

    #from .models import User, Accounts
    # added below because it would not create the tables inside of the database. Will need to comeback to this
    
    class Accounts(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        savings = db.Column(db.Float)
        checkings = db.Column(db.Float)
        date = db.Column(db.DateTime(timezone = True), default=func.now())
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    class User(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        email = db.Column(db.String(150), unique = True)
        password = db.Column(db.String(10))
        firstName = db.Column(db.String(10))
        lastName = db.Column(db.String(10))
        accounts = db.relationship('Accounts')

    create_database(app)
    app.app_context().push()
    db.session.commit()

    return app


def create_database(app):
    if not path.exists('www/'+ DB_NAME):
        db.create_all(app=app)      
        print('Created Database!')
    else:
        print('Database already exists')
