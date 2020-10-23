import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Sql lite database creation with python
basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ --> /myflaskexample/Flask_SQL.py

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

##############################################################

class Puppy(db.Model):
#Manuel table name choice if you want not neccessary
    __tablename__ = 'puppies'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Puppy {self.name} is {self.age} years old"
