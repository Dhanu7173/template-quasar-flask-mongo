from mongoengine import Document, DictField, StringField, DateTimeField, ListField, ObjectIdField
from datetime import datetime

class User(Document):
    meta = {
        'collection': 'users'
    }
    email = StringField(unique=True, required=True, max_length=30)
    password = StringField(min_length=6)
    extra_details = DictField()
    created_at = DateTimeField(default=datetime.utcnow())

    def validator(self):
        return True

