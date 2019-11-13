import json
import requests
from pprint import pprint
import json

headers = { 'Content-Type': 'application/json'}

def get_album():
	api_url = 'https://statsapi.web.nhl.com/api/v1/teams/8/stats'
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
        print(json.dumps(album, indent=2))

else:
        print('[!] Request Failed')

