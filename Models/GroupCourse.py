from peewee import PrimaryKeyField, CharField, IntegerField, ForeignKeyField

from Models import Courses, Professor, TimeCourse
from Models.mainModel import BaseModel


class GroupCourse(BaseModel):
    id = PrimaryKeyField()
    group_number = CharField(45)
    semester = CharField(45)
    guest_semester = CharField(45)
    date_exam = CharField(45)
    time_exam = CharField(45)
    term = CharField(45)
    capacity = IntegerField(11)
    min_capacity = IntegerField(11)
    Course_id = ForeignKeyField(Courses, backref='group_course')
    professor_id = ForeignKeyField(Professor, backref='group_course')
    Time_Course_id = ForeignKeyField(TimeCourse, backref='group_course')

    class Meta:
        db_table = "group_course"

