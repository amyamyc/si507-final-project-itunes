import requests
import json
from app import db
from models import Songs, Genres

# Used Jackie's caching logic from SI506 final project
CACHE_FNAME = "example_cache.json"
try:
    file_obj = open(CACHE_FNAME,'r')
    file_contents = file_obj.read()
    CACHE_DICTION = json.loads(file_contents)
    file_obj.close()
except:
    CACHE_DICTION = {}

def params_unique_combination(baseurl, params_d, private_keys=["api_key"]):
    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            res.append("{}-{}".format(k, params_d[k]))
    return baseurl + "_".join(res)

def get_itunes_data(term, media, limit):
    # add defn of function to get data and return a python object w itunes data...
    baseurl = 'https://itunes.apple.com/search'
    params_diction = {}
    params_diction["term"] = term
    params_diction["media"] = media
    params_diction["limit"] = limit
    # make the request - this is what I dont always wanna do
    unique_identifier = params_unique_combination(baseurl, params_diction) # creating a unique ident for this request
    if unique_identifier in CACHE_DICTION:
        return CACHE_DICTION[unique_identifier]
    else:
        resp = requests.get(baseurl, params=params_diction) # response obj -- I only want to do this once for EACH unique request
        python_object = json.loads(resp.text)
        # Do something else first -- save it for the next time
        cache_file_object = open(CACHE_FNAME, 'w')
        # take the cache dictionary and add a new key-val pair
        CACHE_DICTION[unique_identifier] = python_object
        # I need to make sure that EVERYTHING NOW in the cache dictionary will be saved in my file for next time
        cache_file_object.write(json.dumps(CACHE_DICTION))
        return python_object # return CACHE_DICTION[unique_identifier]

itunes_result_pop = get_itunes_data("Pop", "music", "25")
itunes_result_country = get_itunes_data("Country", "music", "25")
itunes_result_rb = get_itunes_data("HipHop", "music", "25")

def populate_data_into_db(itunes_result): # this is my list # "song" represents each search thing.
    for song in itunes_result:
        if not Genres.query.filter_by(genre = song['primaryGenreName']).first():
            # add new genre using Genres class
            new_genre = Genres(genre = song['primaryGenreName'])
            db.session.add(new_genre)
            db.session.commit()
        # if genre exists in table, check if there is a song in that genre in the Songs table
        if Songs.query.filter_by(name = song["trackName"]).first():
            continue
        else:  # add new song using Songs class
            find_id = Genres.query.filter_by(genre = song['primaryGenreName']).first().id
            new_song = Songs(name = song['trackName'], artist = song['artistName'], album = song['collectionName'], genre_id = find_id )
            db.session.add(new_song)
            db.session.commit()
