from flask import Flask
from server.config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///house.db'
db = SQLAlchemy(app)

print(app.config['SQLALCHEMY_DATABASE_URI'])


from server import routes, models
