from flask import Blueprint, jsonify

# Model
from models.UserModel import UserModel

main = Blueprint('user_blueprint', __name__)


@main.route('/')
def get_users():
    try:
        users = UserModel.get_users()
        return jsonify(users)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
