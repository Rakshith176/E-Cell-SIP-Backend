from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)


app.config['SECRET_KEY']='e8556002376cf2e3d081aab7db746234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

from e_cell import routes