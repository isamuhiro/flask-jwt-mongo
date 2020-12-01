from flask import request, jsonify
from flask_jwt_extended import create_access_token
from mongoengine.errors import NotUniqueError, ValidationError
from database.models import User
from flask_restful import Resource
import datetime


class SignupAPI(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = User(**body)
            user.validate()
            user.hash_password()
            user.save()
            return jsonify(user)

        except NotUniqueError as e:
            return "User already exists!", 409
        except ValidationError as e:
            return e.to_dict(), 422

class LoginAPI(Resource):
    def post(self):
        body = request.get_json()
        user = User.objects.get(email=body.get('email'))
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error': 'Email or password invalid'}, 401

        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)
        return {'token': access_token}, 200
