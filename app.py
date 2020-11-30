from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from settings import load_dotenv

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')

api = Api(app)
bcript = Bcrypt(app)
jwt = JWTManager(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/movie-bag'
}

initialize_db(app)
initialize_routes(api)
app.debug = True
app.run()
