from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'love_si507'
# db.init_app(app)
db = SQLAlchemy(app)

@app.route('/')
def index():
    songs = Songs.query.all()
    num_songs = len(songs)
    return render_template('index.html', num_songs =num_songs)

@app.route('/all_songs')
def see_all():
    all_songs = []
    songs = Songs.query.all()
    for s in songs:
        # genre = Genres.query.filter_by(id=s.genres_id).first() # get just one director instance
        all_songs.append((s.name, s.artist)) # get list of movies with info to easily access [not the only way to do this]
    return render_template('all_songs.html',all_songs=all_songs) # check out template to see what it's doing with what we're sending!

@app.route('/songs/<genre>/') #Put in Country genre
def search_genre(genre):
    all_genres = Genres.query.all() #query all genres. got all them.
    print(all_genres)
    g = Genres.query.filter_by(genre = genre).first() # to match user input
    songs_list = Songs.query.filter_by(genre_id = g.id).all()
    return render_template('genre.html',songs_list =songs_list)

if __name__ == '__main__':
    from SI507_project_tools import *
    db.create_all()
    populate_data_into_db(itunes_result_rb['results'])
    populate_data_into_db(itunes_result_country['results'])
    populate_data_into_db(itunes_result_pop['results'])
    app.run(port=5000, debug=True)
