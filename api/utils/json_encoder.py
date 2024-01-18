import flask
from flask.json.provider import DefaultJSONProvider
from bson import ObjectId
from datetime import datetime
from pymongo.command_cursor import CommandCursor
from mongoengine.queryset.queryset import QuerySet

class JSONEncoder(DefaultJSONProvider):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%dT%H:%M:%SZ')
        if isinstance(o, CommandCursor):
            return [k for k in o]
        if isinstance(o, QuerySet):
            return [k.to_mongo().to_dict() for k in o]
        return DefaultJSONProvider.default(o)

def dictify_document(doc):
    return doc.to_mongo().to_dict()