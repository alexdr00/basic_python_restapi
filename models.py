from mongoengine import *


class Post(Document):
    title = StringField(required=True)
    description = StringField(required=True, min_length=20)
    tags = ListField(StringField(max_length=20))


class User(Document):
    name = StringField(required=True)
    email = EmailField()
