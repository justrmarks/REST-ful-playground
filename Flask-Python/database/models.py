from .db import db

class Song(db.Document):
    name = db.StringField(required=True, unique=True)
    album = db.StringField(required=True)
    artists = db.ListField(db.StringField(), required=True)
    genres = db.ListField(db.StringField(), required=True)
    audio = db.FileField()