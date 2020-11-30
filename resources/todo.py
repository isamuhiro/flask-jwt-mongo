from flask import Response, request
from flask_restful import Resource
from database.models import Todo    


class TodosAPI(Resource):
    def get(self):
        todos = Todo.objects().to_json()
        return Response(todos, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        todo = Todo(**body).save()
        return {'id': str(todo.id)}, 200


class TodoAPI(Resource):
    def put(self, id):
        body = request.get_json()
        Todo.objects.get(id=id).update(**body)
        return '', 200

    def delete(self, id):
        todo = Todo.objects.get(id=id).delete()
        return '', 200

    def get(self, id):
        todo = Todo.objects.get(id=id).to_json()
        return Response(todo, mimetype="application/json", status=200)
