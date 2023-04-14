import requests

CLIENT_ID = 'e44cfc4e30924ea98a0ae67a6260fb6c'
CLIENT_SECRET = '5feb722ab9fb4ec8b539f0417492ae4c'
AUTH_URL = 'https://accounts.spotify.com/api/token'


auth_response = requests.post(
    AUTH_URL, {
    'grant_type' : 'client_credentials',
    'client_id' : CLIENT_ID,
    'client_secret' : CLIENT_SECRET,
    }
)
auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']
#print(access_token)
headers = {
    'Authorization' : 'Bearer {token}'.format(token=access_token)
}

BASE_URL = 'https://api.spotify.com/v1/'

track_id = '3JjnGLK8IxkNLvo8Lb3KOM'

r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
r = r.json()

for key in r:
    print(key , ":", r[key])