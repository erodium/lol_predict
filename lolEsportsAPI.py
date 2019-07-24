import json, requests

apiEndpoint = "https://api.lolesports.com/api/"

LEAGUE_SLUGS = [None, "all-star", "na-lcs", "eu-lcs", "na-cs", "eu-cs", "lck", "lpl-china", "lms", "worlds", "msi"]


class Season():

    def __init__(self, tournament):
        self.title = tournament['title']
        self.description = tournament['description']
        self.id = tournament['id']
        self.teams = tournament['rosters']
        self.brackets = tournament['brackets']
        self.games = tournament['gameIds']
        self.leagueId = tournament['league']

    #    def __repr__(self):
    #        return ("Season({},{},{})".format(
    #            self.title, self.description, self.id))

    def __str__(self):
        return "title: {}\ndescription: {}\nid: {}".format(self.title, self.description, self.id)

    def getMatches(self):
        return (self.games)

    def getID(self):
        return (self.id)


def getLeagueId(slug):
    if isinstance(slug, str) and slug in LEAGUE_SLUGS:
        return (LEAGUE_SLUGS.index(slug))
    else:
        return ("error: invalid slug in getLeagueId")


def getLeagues(_id=None, slug=None):
    if (_id == None and slug == None):
        r = requests.get(apiEndpoint + "v1/leagues").json()
    elif (_id == None and slug != None):
        r = requests.get(apiEndpoint + "v1/leagues?slug=" + str(slug)).json()
    elif (_id != None and slug == None):
        r = requests.get(apiEndpoint + "v1/leagues?id=" + str(_id)).json()
    elif (_id != None and slug != None):
        r = requests.get(apiEndpoint + "/v1/leagues?id=" + str(_id) + "?slug=" + str(slug)).json()
    return r


def writeLeagueInfo(id):
    if isinstance(id, str) and id in LEAGUE_SLUGS:
        id = getLeagueId(id)
    league_object = getLeagues(_id=id)
    with open("league" + str(id) + ".json", "w") as writefile:
        json.dump(league_object, writefile)


# get json info for each league from api/vi/leagues
def getAllLeagueInfo():
    for slug in LEAGUE_SLUGS:
        writeLeagueInfo(slug)


# checking league 10
# r = requests.get("https://api.lolesports.com/api/v1/leagues?id=10", stream=True).json()
# with open ("league10.json", "w") as writefile:
#	writefile.write(json.dumps(r))
#	print(r)

def getTournaments(leagueId):
    if isinstance(leagueId, str) and leagueId in LEAGUE_SLUGS:
        leagueId = getLeagueId(leagueId)
    if isinstance(leagueId, int) and leagueId > 0 and leagueId < len(LEAGUE_SLUGS):
        r = requests.get(apiEndpoint + "v2/highlanderTournaments?league=" + str(leagueId), stream=True).json()
    else:
        r = {'error': 'invalid leagueID in getTournaments'}
    return r


def writeTournyInfo(id):
    tourny_object = getTournaments(id)
    if 'error' not in tourny_object.keys():
        with open("league" + str(id) + "_tournaments.json", "w") as writefile:
            json.dump(tourny_object, writefile)
        return 0
    else:
        return tourny_object['error']


# get tournament info from api/v2/highlanderTournaments
def getAllTournamentInfo():
    for tnmt in range(1, 11):
        result = writeTournyInfo(tnmt)
        print("{} result {}".format(tnmt, result))


def getTournamentInfo(id):
    if isinstance(id, str) and id in LEAGUE_SLUGS:
        id = LEAGUE_SLUGS.index(id)
    with open("league" + str(id) + "_tournaments.json", "r") as readfile:
        league_object = json.load(readfile)
    # print("gti {}".format(type(league_object)))
    # print(league_object.keys())
    return league_object


def getSeasonInfo(tourny, id):
    # print("a {}".format(type(tourny)))
    if isinstance(tourny, str):
        # print("here")
        tourny = json.load(tourny)
    # print("b {}".format(type(tourny[id])))
    if isinstance(id, int) and id >= 0 and id < len(tourny['highlanderTournaments']):
        return tourny['highlanderTournaments'][id]
    else:
        return ("error in getSeasonInfo")


def getAllSeasons(tourny):
    if isinstance(tourny, str):
        tourny = json.load(tourny)
    seasonList = tourny['highlanderTournaments']['brackets']
    seasons = []
    for bracketId, bracketDetails in seasonList.items():
        season.append(bracketDetails)
    return seasons


def getMatchDetails(tournamentId, matchId):
    endpoint = apiEndpoint + "v2/highlanderMatchDetails?tournamentId=" + str(tournamentId) + "&matchId=" + str(matchId)
    print("getting {} match {} from {}".format(tournamentId, matchId, endpoint))
    r = requests.get(endpoint).json()
    return r


# uncomment the below line to write all files anew.
# getAllTournamentInfo()
# for league in LEAGUE_SLUGS:
#    tourn = getTournamentInfo(league)
#    lo = getSeasonInfo(tourn, 0)

# s = Season(lo)

# print("lo {}".format(type(lo)))
# print(s)
# matches = s.getMatches()
# print(s.getID())
# print(getMatchDetails(s.getID(), matches[0]))
"""
for league in LEAGUE_SLUGS:
    print(league)
    if league is None:
        print("none")
    else:
        tourn = getTournamentInfo(league)
        seasonsInfo = getAllSeasons(tourn)
        for bracket in seasonsInfo:
            print("{},{}".format(bracket['name']))
            for matchId in season['gameIds']:
                if index < 3:
                    matchDetails = getMatchDetails(season['id'], matchId)
                    print(matchDetails)
                    index += 1
                else: break




tourn = getTournamentInfo("worlds")
seasons = getAllSeasons(tourn)
for season in seasons:
    if season['id'] != "91be3d78-874a-44e0-943f-073d4c9d7bf6":
        print("no")
    else:
        for matchId in season['gameIds']:
            if matchId != "22851f97-7555-494d-b234-1e4bbeaf8dd5":
                print("nope")
            else:
                matchDetails = getMatchDetails(season['id'], matchId)
                print(matchDetails)
"""
