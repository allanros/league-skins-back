from flask import Flask
from src.main.routes.user_routes import user_routes
from src.main.routes.champions_routes import champions_routes

app = Flask(__name__)
app.register_blueprint(user_routes)
app.register_blueprint(champions_routes)
