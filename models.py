from app import db

class Songs(db.Model):
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True) #1, 2, 3
    name = db.Column(db.String(250), nullable=False) #song name "Make it Better"
    artist = db.Column(db.String(250), nullable=False)
    album = db.Column(db.String(250), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.id")) #references the genres (name of the table) table. the name of the table followed by name of column

    genres = db.relationship("Genres", backref="songs")

    def __init__(self, name = None, artist = None, album = None, genre_id = None, songs_dict = None):
        self.name = name # name of song
        self.artist = artist
        self.album = album
        self.genre_id = genre_id
        if songs_dict:  # rewrite __init__() to accept raw dict as input for constructor
            self.name = songs_dict['results'][0]['trackName']
            self.artist = songs_dict['results'][0]['artistName']
            self.album = songs_dict['results'][0]['collectionName']
            self.song_id = songs_dict['results'][0]["trackId"]

    def __repr__(self):  # rewrite __repr__() to show user-friendly info # Crazy in Love by Beyonce
        return "{song_name} by {artist_name}".format(
            song_name = self.name,
            artist_name = self.artist
        )

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class Genres(db.Model):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(250))

    def __init__(self, genre = None, genre_dict = None):
        self.genre = genre
        if genre_dict: # rewrite __init__() to accept raw dict as input for constructor
            self.genre = genre_dict['results'][0]['primaryGenreName']

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
