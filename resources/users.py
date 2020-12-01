from flask import jsonify
from database.models import User
from flask_restful import Resource

class UsersAPI(Resource):
    def get(self):
        users = User.objects()
        quantity = users.count()
        for user in users:
            print(user.to_json())
        return jsonify(users)
