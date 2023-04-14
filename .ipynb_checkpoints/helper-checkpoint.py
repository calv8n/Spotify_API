import time
import spotipy
from IPython.core.display import clear_output
from spotipy import SpotifyClientCredentials, util

CLIENT_ID = 'e44cfc4e30924ea98a0ae67a6260fb6c'
CLIENT_SECRET = '5feb722ab9fb4ec8b539f0417492ae4c'
AUTH_URL = 'https://accounts.spotify.com/api/token'
USERNAME = 'x10f40rjposgn1b30n110vwk3'
SCOPE = 'playlist-modify-public'

credentials = SpotifyClientCredentials(CLIENT_ID,CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=credentials)

token = util.prompt_for_user_token(USERNAME,SCOPE,CLIENT_ID,CLIENT_SECRET,AUTH_URL)
spt = spotipy.Spotify(auth=token)

def album_id(ids):
    album_ids = []
    results = sp.artist_albums(ids)
    for album in results['items']:
        album_ids.append(album['id'])
    return album_ids

def album_song_id(ids):
    song_ids = []
    results = sp.album_tracks(ids,offset=0)
    for song in results['items']:
        song_ids.append(song['id'])
    return song_ids

def song_features(ids):
    meta = sp.track(ids)
    features = sp.audio_features(ids)

    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity']
    ids = meta['id']

    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    valence = features[0]['valence']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    key = features[0]['key']
    time_signature = features[0]['time_signature']

    track = [name, album, artist, ids, release_date, popularity, length, danceability, acousticness,
            energy, instrumentalness, liveness, valence, loudness, speechiness, tempo, key, time_signature]
    columns = ['name','album','artist','id','release_date','popularity','length','danceability','acousticness','energy','instrumentalness',
                'liveness','valence','loudness','speechiness','tempo','key','time_signature']
    return track,columns

def song_artist_ids_playlist(ids):
    playlist = sp.playlist_tracks(ids)
    songs_id = []
    artists_id = []
    for result in playlist['items']:
        songs_id.append(result['track']['id'])
        for artist in result['track']['artists']:
            artists_id.append(artist['id'])
    return songs_id, artists_id
