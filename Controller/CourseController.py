from flask_restful import Resource, reqparse, abort
from flask import g
from Models import ChoiceCourse
from Models.Courses import Course

from Auth.Auth import auth2

class list(Resource):
    @auth2.login_required
    def get(self):
        courses = Course.select()
        ls = [dict(
            id=c.id,
            presentation=c.presentation,
            type=c.type,
            status_prerequisite=c.status_prerequisite,
            name=c.name,
            unit_number=c.unit_number,
            price=c.price,
            list_prerequisite=c.list_prerequisite,
        ) for c in courses]
        return dict(courses=ls)


class Delete(Resource):
    @auth2.login_required
    def delete(self):
        return dict(
            status=ChoiceCourse.delete().where(
                ChoiceCourse.Student_student_number_id == g.user.student_number).execute()
        )