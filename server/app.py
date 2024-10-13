from flask_sqlalchemy import SQLALchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_RRI'] = 'sqlite:///info.db'

