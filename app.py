import os
from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from settings import load_dotenv

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")
app.config['MONGODB_SETTINGS'] = { 'host': os.getenv("DB_HOST") }

api = Api(app)
bcript = Bcrypt(app)
jwt = JWTManager(app)


initialize_db(app)
initialize_routes(api)
app.debug = True
app.run()
