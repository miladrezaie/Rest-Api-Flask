from flask import Flask
from flask_restful import Api

from routes import route
app = Flask(__name__)
api = Api(app)


route.route(api)


if __name__ == '__main__':
    app.run(debug=True)
