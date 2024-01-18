__author__ = 'Phantom'

import config, flask
from flask_cors import CORS
from mongoengine import connect
from utils.json_encoder import JSONEncoder
from utils.route_helper import exception_handler
from views import main_bp

app = flask.Flask(__name__)
app.secret_key = config.SECRET_KEY

app.from_pyfile('config.py')

# app.config['DEBUG'] = config.DEBUG
# app.config['MAX_CONTENT_LENGTH'] = config.MAX_CONTENT_LENGTH

app.json = JSONEncoder(app)
app.errorhandler(exception_handler)
app.register_blueprint(main_bp)

CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

connect(db=config.MONGO_DBNAME, host=config.MONGO_DBURI)

if __name__ == '__main__':
    app.run(port=config.FLASK_PORT)
