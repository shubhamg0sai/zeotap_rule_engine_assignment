from flask import Flask

# Create a flask instance
def create_app():
    app = Flask(__name__)

    with app.app_context():
        from . import apirun
        apirun.init_app(app)

    return app