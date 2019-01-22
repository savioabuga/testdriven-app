import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app_config = os.getenv("APP_SETTINGS")

app.config.from_object(app_config)

db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean, default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email


@app.route("/users/ping", methods=["GET"])
def hello():
    return jsonify({"message": "pong!", "status": "success"})
