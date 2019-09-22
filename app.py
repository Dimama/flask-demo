from os import environ

from api import create_app

from config import HOST, PORT, DEBUG


if __name__ == "__main__":
    app = create_app()
    app.run(host=HOST, port=environ.get("PORT", PORT), debug=DEBUG)
