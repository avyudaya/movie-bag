from flask import Flask
from flask_bcrypt import Bcrypt
from database.db import initialize_db
from resources.routes import initialize_routes
from flask_restful import Api
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost:27017/movie-bag'
}

initialize_db(app)
initialize_routes(api)

app.run()