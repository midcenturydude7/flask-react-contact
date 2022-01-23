import os
from flask import *
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


file_path = os.path.abspath(os.getcwd())+"\database.db"


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

@app.route('/ping')
def ping():
    return ("Hello, World!")


if __name__ == '__main__':
    app.run()
