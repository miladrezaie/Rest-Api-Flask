from passlib.handlers.bcrypt import bcrypt
import env
from Models import mainModel
from Models.mainModel import EnumField
from peewee import IntegerField, TextField, CharField, PrimaryKeyField
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

class Student(mainModel.BaseModel):
    firstname = CharField()
    lastname = CharField()
    father = CharField()
    brithday = CharField()
    location_brith = CharField()
    phone = CharField()
    mobile = CharField()
    national_code = CharField()
    status = EnumField(choices=['active', 'non_active', 'expulsion', 'alumnus'])
    entry_semester = CharField()
    img = CharField()
    address = TextField()
    student_number = PrimaryKeyField(unique=True)
    id = CharField(11)
    password = CharField(100)

    class Meta:
        db_table = "student"
        order_by = ('student_number',)

    def hash_password(self, password):
        self.password = bcrypt.hash(password)

    # verify_password is func verify baresiejat
    def verify_password(self, password):
        return bcrypt.verify(password, self.password)

    # create token
    def generate_auth_token(self, expiration=600):
        s = Serializer(env.secret_key, expires_in=expiration)
        return s.dumps({'id': self.id})

    def verify_auth_token(token):
        # check as secretkey with token
        s = Serializer(env.secret_key)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token غیر مجاز
        try:
            user = Student.get(Student.id == data['id'])
            return user
        except:
            return None  # not find id
