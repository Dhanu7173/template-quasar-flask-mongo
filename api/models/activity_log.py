from mongoengine import Document, DictField, StringField, DateTimeField, ListField, ObjectIdField, ReferenceField
from datetime import datetime
from .user import User

class ActivityLog(Document):
    meta = {
        'collection': 'activity_logs'
    }
    activity = StringField(required=True)
    extra_details = DictField()
    created_by = ReferenceField(User)
    created_at = DateTimeField(default=datetime.utcnow())

    def validator(self):
        return True
    