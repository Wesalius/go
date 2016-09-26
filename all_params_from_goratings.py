import urllib.request, json

with urllib.request.urlopen("http://www.goratings.org/ratings.json") as url:
	response = url.read()
	elo_data = json.loads(response.decode('utf-8'))

for num in range(0,827):
	rank = (elo_data["ratings"][num]["RANK"])
	id = (elo_data["ratings"][num]["ID"])
	name = (elo_data["ratings"][num]["NAME"])
	rating = (elo_data["ratings"][num]["RATING"])
	print(rank,id,name,rating)