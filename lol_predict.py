import lol
import json
import lolEsportsAPI

LEAGUE_SLUGS = [None, "all-star", "na-lcs", "eu-lcs", "na-cs", "eu-cs", "lck", "lpl-china", "lms", "worlds", "msi"]

with open("league2.json", "r") as readfile:
    league_object = json.load(readfile)

lcs = lol.League(league_object)

matchList = lcs.listAllMatches()

index = 0
for tournament in matchList:
    for tournyId, matchIdList in tournament.items():
        for matchId in matchIdList:
            if index < 5:
                r = lolEsportsAPI.getMatchDetails(tournyId, matchId)
                print(r)
                index += 1
            else:
                break
        if index > 4:
            break
