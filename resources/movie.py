from flask import Response, request
from flask import jsonify
from flask_restful import Resource
from database.models import Movie
from flask_jwt_extended import jwt_required


class MoviesApi(Resource):
    def get(self):
        movies = Movie.objects()
        return jsonify(movies)

    @jwt_required
    def post(self):
        body = request.get_json()
        movie = Movie(**body).save()
        id = movie.id
        return {'id': str(id)}, 200


class MovieApi(Resource):
    @jwt_required
    def put(self, id):
        body = request.get_json()
        Movie.objects.get(id=id).update(**body)
        return '', 200

    @jwt_required
    def delete(self, id):
        movie = Movie.objects.get(id=id).delete()
        return '', 200

    def get(self, id):
        movies = Movie.objects.get(id=id)
        return jsonify(movies)
