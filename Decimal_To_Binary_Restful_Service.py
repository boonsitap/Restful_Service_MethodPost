from flask import Flask , request
from flask_restful import Resource , Api, reqparse
import json ,time

app = Flask (__name__)
api = Api(app)

def convertToBinary(decimal):
    return "{0:b}".format(decimal)

parser = reqparse.RequestParser()
parser.add_argument('studendId')

class id(Resource):
        def get(self):
            return {"message": "Enter your student ID"}
        def post(self):
                args = parser.parse_args()
		studentId = args['studendId']
		numbin = convertToBinary(studentId)
		return {"StudentID": studendId,"Binary": numbin}

api.add_resource(id,'/api/id')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5500)
