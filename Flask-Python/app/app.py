from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Song

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/song-crate'
}

db = initialize_db(app)

# index
@app.route('/songs')
def get_songs():
    songs = Song.objects().to_json()
    return Response(movies, mimetype="application/json", status=200)

# create
@app.route('/songs', methods=['POST'])
    body = request.get_json()
    song = Song(**body).save()
    id = song.id
    return {'id': str(id)}, 200

# read
@app.route('/movies/<id>')
def get_song(id):
    movies = Movie.objects.get(id=id).to_json()
    return Response(movies, mimetype="application/json", status=200)

# Update
def update_movie(id):
    body = request.get_json()
    Movie.objects.get(id=id).update(**body)
    return '', 200

# Delete
@app.route('/movies/<id>', methods=['DELETE'])
def delete_movie(id):
    Movie.objects.get(id=id).delete()
    return '', 200

app.run()