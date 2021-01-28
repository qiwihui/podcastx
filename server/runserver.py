
from config import BaseConfig
from app import create_app, add_api_support


flask_app = create_app(BaseConfig)
flask_app = add_api_support(flask_app)


if __name__ == '__main__':
    import os
    flask_app.secret_key = os.urandom(24)
    flask_app.run(debug=True)
