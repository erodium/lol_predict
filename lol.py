class Team:

    def __init__(self, body="empty"):
        self.body = body
        if "roster" in body.keys():
            self.id = body["roster"]


class Match:

    def __init__(self, body="empty"):
        self.teams = []
        self.body = body
        self.id = body["id"]
        for team in body["input"]:
            self.teams.append(Team(team))

    def __str__(self):
        return str(self.body)

    def getMatchId(self):
        return self.id


class Bracket:

    def __init__(self, body="empty"):
        self.matches = []
        self.body = body
        self.id = body["id"]
        self.name = body["name"]
        for id, match in body["matches"].items():
            self.matches.append(Match(match))

    def getMatchList(self):
        matchList = []
        for match in self.matches:
            matchList.append(match.id)
        return (matchList)


class Tournament:

    def __init__(self, body="empty"):
        self.brackets = []
        self.body = body
        self.id = body["id"]
        self.title = body["title"]
        self.description = body["description"]
        self.roster = body["rosters"]
        for id, bracket in body["brackets"].items():
            self.brackets.append(Bracket(bracket))

    def __str__(self):
        return self.title

    def getMatchList(self):
        tournamentMatchList = []
        for bracket in self.brackets:
            for matchId in bracket.getMatchList():
                tournamentMatchList.append(matchId)
        return ({self.id: tournamentMatchList})


class League:

    def __init__(self, body="empty"):
        self.tournaments = []
        self.body = body
        self.id = body["leagues"][0]["id"]
        self.slug = body["leagues"][0]["slug"]
        self.guid = body["leagues"][0]["guid"]
        self.region = body["leagues"][0]["region"]
        self.tournamentIds = body["leagues"][0]["tournaments"]
        for tournament in body["highlanderTournaments"]:
            self.tournaments.append(Tournament(tournament))

    def __str__(self):
        return "{}, {}:{}".format(self.slug, self.guid, self.id)

    def getTournaments(self):
        return (self.tournaments)

    def listTournaments(self):
        tournamentList = []
        for tournament in self.tournaments:
            tournamentList.append(str(tournament))
        return (tournamentList)

    def listAllMatches(self):
        leagueMatchList = []
        for tournament in self.tournaments:
            leagueMatchList.append(tournament.getMatchList())
        return (leagueMatchList)


class Lol:
    leagues = []
    body = "empty lol"

    def __init__(self, body):
        self.body = body
