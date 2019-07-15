import json, requests

otherEndpoint="http://leagues.lolesports.com/api/v1/leagues/"

LEAGUE_SLUGS = ["none", "all-star", "na-lcs", "eu-lcs", "na-cs", "eu-cs", "lck", "lpl-china", "lms", "worlds", "msi"]

def getLeagues(_id=None, slug=None):
	if(_id == None and slug == None):
		r = requests.get("https://api.lolesports.com/api/v1/leagues").json()
	elif(_id == None and slug != None):
		r = requests.get("https://api.lolesports.com/api/v1/leagues?slug=" + str(slug)).json()
	elif(_id != None and slug == None):
		r = requests.get("https://api.lolesports.com/api/v1/leagues?id=" + str(_id)).json()
	elif(_id != None and slug != None):
		r = requests.get("https://api.lolesports.com/api/v1/leagues?id=" + str(_id) + "?slug=" + str(slug)).json()
	return r

def writeLeagueInfo(id):
	league_object = getLeagues(_id=id)
	with open ("league"+str(id)+".json", "w") as writefile:
		writefile.write(json.dumps(league_object))

#for id in range(0,10):
#	getAllLeagues(id)

r = requests.get("https://api.lolesports.com/api/v1/leagues?id=0", stream=True).json()
with open ("league0.json", "w") as writefile:
	writefile.write(json.dumps(r))
	print(r)


