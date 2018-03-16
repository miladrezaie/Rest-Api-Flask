from Controller import CourseController, LoginController
from passlib.handlers import bcrypt



def route(api):
    api.add_resource(CourseController.list, '/a')
    api.add_resource(LoginController.Login, '/login')


