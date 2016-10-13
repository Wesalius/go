import json
import urllib.request

from item_player_pairs import wd_items

with urllib.request.urlopen("http://www.goratings.org/ratings.json") as url:
	response = url.read()
	go_ratings_data = json.loads(response.decode('utf-8'))

l = list(wd_items)
v = list(wd_items.values())

for key in go_ratings_data["ratings"]:
	if(key.get("NAME") in l):
	    print(key.get("NAME"))