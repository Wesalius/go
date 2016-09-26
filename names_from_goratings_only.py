import urllib.request, json

with urllib.request.urlopen("http://www.goratings.org/ratings.json") as url:
	response = url.read()
	elo_data = json.loads(response.decode('utf-8'))

for num in range(0,828):
	name = (elo_data["ratings"][num]["NAME"])
	print(name)