from datetime import timedelta
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from src.main.routes.user_routes import user_routes
from src.main.routes.champions_routes import champions_routes

app = Flask(__name__)
CORS(app)
app.config["JWT_SECRET_KEY"] = "secret_key"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)
jwt = JWTManager(app)

app.register_blueprint(user_routes)
app.register_blueprint(champions_routes)
