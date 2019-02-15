from flask import Blueprint, jsonify, request, render_template
from sqlalchemy import exc
from project import db
from project.api.models import User
from project.api.utils import authenticate

users_blueprint = Blueprint("users", __name__, template_folder="./templates")


@users_blueprint.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        db.session.add(User(username=username, email=email, password=password))
        db.session.commit()

    users = User.query.all()
    return render_template("index.html", users=users)


@users_blueprint.route("/users/ping", methods=["GET"])
def ping_pong():
    return jsonify({"message": "pong!", "status": "success"})


@users_blueprint.route("/users", methods=["POST"])
@authenticate
def add_user(resp):
    post_data = request.get_json()
    response_object = {"status": "fail", "message": "Invalid payload."}
    if not post_data:
        return jsonify(response_object), 400
    username = post_data.get("username")
    email = post_data.get("email")
    password = post_data.get("password")
    try:
        user = User.query.filter_by(email=email).first()
        if not user:
            db.session.add(User(username=username, email=email, password=password))
            db.session.commit()
            response_object["status"] = "success"
            response_object["message"] = f"{email} was added!"
            return jsonify(response_object), 201
        else:
            response_object["message"] = "Sorry. That email already exists."
            return jsonify(response_object), 400
    except (exc.IntegrityError, ValueError):
        db.session.rollback()
        return jsonify(response_object), 400


@users_blueprint.route("/users/<user_id>")
def get_single_user(user_id):
    response_object = {"status": "fail", "message": "User does not exist"}

    try:
        user = User.query.filter_by(id=int(user_id)).first()
        if not user:
            return jsonify(response_object), 404
        else:
            response_object = {
                "status": "success",
                "data": {
                    "id": user.id,
                    "active": user.active,
                    "email": user.email,
                    "username": user.username,
                },
            }
            return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404

    return jsonify(response_object), 200


@users_blueprint.route("/users", methods=["GET"])
def get_users():
    response_object = {
        "status": "success",
        "data": {"users": [user.to_json() for user in User.query.all()]},
    }
    return jsonify(response_object), 200
