import json
import requests
from pprint import pprint

api_token = 'BQB3Dr9NqHxXY6-kaGxX2vfbXdMUCZLqv8fZZ8D0PhKGA66GAvvG97eVyATrMGVnFTFxzWZmHtr67CXxIPhmS3iLn785PXXEwrU2Gv0KJwZCLRSkBCoHvm8V12_r_9dcxkIDRIxDPXzVImQ'
api_url_base = 'https://api.spotify.com/'
headers = { 'Content-Type': 'application/json',
			'Authorization': 'Bearer {0}'.format(api_token)}

def get_album():
	api_url = '{0}v1/artists/2yEwvVSSSUkcLeSTNyHKh8/albums'.format(api_url_base)
	response = requests.get(api_url, headers=headers)

	pprint(api_url)
	pprint(response)

	if response.status_code == 200:
		return json.loads(response.content.decode('utf-8'))
	else:
		return None

album_info = get_album()

if album_info is not None:
    print("Here's your info: ")
    for album in album_info.items():
        print(album)

else:
        print('[!] Request Failed')

