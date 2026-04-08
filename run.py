"""Application entry point."""
from dotenv import load_dotenv

from flask_starterkit.main.app import flask_app

if __name__ == "__main__":
    load_dotenv(dotenv_path="./.env")
    flask_app.run()
