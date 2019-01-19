from flask import Flask, jsonify

app = Flask(__name__)

app.config.from_object("project.config.DevelopmentConfig")


@app.route("/users/ping", methods=["GET"])
def hello():
    return jsonify({"message": "pong!", "status": "success"})
