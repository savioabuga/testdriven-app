import os
from flask import Flask, jsonify

app = Flask(__name__)

app_config = os.getenv("APP_SETTINGS")

app.config.from_object(app_config)


@app.route("/users/ping", methods=["GET"])
def hello():
    return jsonify({"message": "pong!", "status": "success"})
