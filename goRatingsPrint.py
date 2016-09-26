import urllib.request, json
with urllib.request.urlopen("http://www.goratings.org/ratings.json") as url: #source of data
	response = url.read()
	go_ratings_data = json.loads(response.decode('utf-8'))
	print(go_ratings_data)