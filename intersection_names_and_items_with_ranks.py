import urllib.request, json
from item_player_pairs import wd_items
from datetime import date

with urllib.request.urlopen("http://www.goratings.org/ratings.json") as url: #source of data
	response = url.read()
	go_ratings_data = json.loads(response.decode('utf-8')) #assigning fetched data to variable

today = date.today()
l = list(wd_items)
v = list(wd_items.values())

for key in go_ratings_data["ratings"]:
	if(key.get("NAME") in l):
	    print(key.get("NAME")," ",v[l.index(key.get("NAME"))],"\tP1087\t+",key.get("RATING"),"\tP813\t+",today,"T00:00:00Z/11\tS248\tQ23058744",sep="")