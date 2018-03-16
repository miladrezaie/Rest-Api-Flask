from flask import g
from flask_restful import Resource
from Auth.Auth import auth

#
# class Login(Resource):
#     @auth.login_required
#     def get(self):
#         token = g.user.generate_auth_token(600)
#         return {'token': token.decode('ascii'), 'duration': 600, 'lastname': g.user.lastname}
#
#     @auth.login_required
#     def post(self):
#         token = g.user.generate_auth_token(600)
#         return {'token': token.decode('ascii'), 'duration': 600, 'lastname': g.user.lastname}

class Login(Resource):
    @auth.login_required
    def get(self):
        token = g.user.generate_auth_token(600)
        return {'token': token.decode('ascii'), 'duration': 600}

    @auth.login_required
    def post(self):
        token = g.user.generate_auth_token(600)
        return {'token': token.decode('ascii'), 'duration': 600}
