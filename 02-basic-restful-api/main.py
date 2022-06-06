from flask import Flask
from flask import render_template, jsonify, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):

    def get(self):
        return {'hello': 'world'}

    def post(self):
        postedData = request.get_json()
        print(f"received data:{postedData}")
        # do something with the data
        result = {
            'Message': "success",
            'Status Code': 200
        }
        return jsonify(result)

api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(debug=True)