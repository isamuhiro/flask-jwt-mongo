from .movie import MoviesApi, MovieApi
from .todo import TodoAPI, TodosAPI
from .auth import SignupAPI, LoginAPI
from .users import UsersAPI


def initialize_routes(api):
    api.add_resource(MoviesApi, '/api/movies')
    api.add_resource(MovieApi, '/api/movies/<id>')
    api.add_resource(TodosAPI, '/api/todos')
    api.add_resource(TodoAPI, '/api/todos/<id>')
    api.add_resource(SignupAPI, '/api/signup')
    api.add_resource(LoginAPI, '/api/login')
    api.add_resource(UsersAPI, '/api/users')
