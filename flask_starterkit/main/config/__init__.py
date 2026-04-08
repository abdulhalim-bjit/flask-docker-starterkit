"""Flask application factory configuration."""
import os
from flask import Flask
from flask_starterkit.main.routes import auth


def create_app():
    """Create and configure the Flask application instance.

    You can also pass any config, blueprints or commands inside this function.

    Returns:
        Flask: The configured instance of the flask application
    """
    app_instance = Flask(__name__)
    app_instance.config["YOUR_AWESOME_CONFIG_ENV"] = "your awesome non sensitive value"
    # app_instance.config["YOUR_SUPER_SECRET_VALUE"] = os.getenv(
    #     "FAKE_SUPER_SECRET")
    app_instance.register_blueprint(auth.auth_routes, url_prefix="/api/auth")
    return app_instance
