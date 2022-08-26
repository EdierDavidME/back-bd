from flask import Flask, jsonify
from config import config

# Routes
from routes import User

# INICIAR SERVER
app = Flask(__name__)


def page_not_found(error):
    return jsonify({"message": "Not found page", "status": 404})


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(User.main, url_prefix='/api/v1/users')

    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()
