import json, requests

apiEndpoint = "https://api.lolesports.com/api/"


LEAGUE_SLUGS = ["none", "all-star", "na-lcs", "eu-lcs", "na-cs", "eu-cs", "lck", "lpl-china", "lms", "worlds", "msi"]

def getLeagueId(slug):
	if isinstance(slug, str) and slug in LEAGUE_SLUGS:
		return(LEAGUE_SLUGS.index(slug))
	else:
		return("error: invalid slug in getLeagueId")

def getLeagues(_id=None, slug=None):
	if(_id == None and slug == None):
		r = requests.get(apiEndpoint+"v1/leagues").json()
	elif(_id == None and slug != None):
		r = requests.get(apiEndpoint+"v1/leagues?slug=" + str(slug)).json()
	elif(_id != None and slug == None):
		r = requests.get(apiEndpoint+"v1/leagues?id=" + str(_id)).json()
	elif(_id != None and slug != None):
		r = requests.get(apiEndpoint+"/v1/leagues?id=" + str(_id) + "?slug=" + str(slug)).json()
	return r

def writeLeagueInfo(id):
	if isinstance(leagueId, str) and leagueId in LEAGUE_SLUGS:
		leagueId = LEAGUE_SLUGS.index(leagueId)
	league_object = getLeagues(_id=id)
	with open ("league"+str(id)+".json", "w") as writefile:
		writefile.write(json.dumps(league_object))

# get json info for each league from api/vi/leagues
#def getAllLeagueInfo():
	#for id in range(0,10):
	#	writeLeagueInfo(id)

# checking league 10
#r = requests.get("https://api.lolesports.com/api/v1/leagues?id=10", stream=True).json()
#with open ("league10.json", "w") as writefile:
#	writefile.write(json.dumps(r))
#	print(r)

def getTournaments(leagueId):
	if isinstance(leagueId, str) and leagueId in LEAGUE_SLUGS:
		leagueId = LEAGUE_SLUGS.index(leagueId)
	if isinstance(leagueId, int) and leagueId > 0 and leagueId < len(LEAGUE_SLUGS):
		r = requests.get(apiEndpoint+"v2/highlanderTournaments?league=" + str(leagueId), stream=True).json()
	else:
		r = {'error':'invalid leagueID in getTournaments'}
	return r

def writeTournyInfo(id):
	tourny_object = getTournaments(id)
	if 'error' not in tourny_object.keys():
		with open ("league"+str(id)+"_tournaments.json", "w") as writefile:
			writefile.write(json.dumps(tourny_object))
		return 0
	else:
		return tourny_object['error']

# get tournament info from api/v2/highlanderTournaments
def getAllTournamentInfo():
	for tnmt in range (1,11):
		result = writeTournyInfo(tnmt)
		print ("{} result {}".format(tnmt, result))

#getAllTournamentInfo()

def getMatchList(id):
	with open("league"+str(id)+"_tournaments.json", "r") as readfile:
		league_object = readfile.readlines()
	return league_object

lo = getMatchList(2)
print(lo)