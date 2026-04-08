"""Authentication routes blueprint."""
from flask import Blueprint

auth_routes = Blueprint("auth_routes", __name__)


@auth_routes.route('/')
def welcome():
    """Return a welcome message for the auth endpoint."""
    return {
        "message": "Welcome to your awesome auth endpoint",
        "success": True
    }
