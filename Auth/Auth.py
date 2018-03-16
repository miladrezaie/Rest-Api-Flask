from flask import g
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from Models.Student import Student

auth = HTTPBasicAuth()
auth2 = HTTPTokenAuth()


# noinspection PyBroadException
@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = Student.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        try:
            user = Student.get(Student.student_number == username_or_token)
        except:
            user = None
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


@auth2.verify_token
def verify_token(token):
    user = Student.verify_auth_token(token)
    if user:
        g.user = user
        return True
    return False
