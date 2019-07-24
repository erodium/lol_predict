import lol
import json

LEAGUE_SLUGS = [None, "all-star", "na-lcs", "eu-lcs", "na-cs", "eu-cs", "lck", "lpl-china", "lms", "worlds", "msi"]

with open("league2.json", "r") as readfile:
    league_object = json.load(readfile)

lcs = lol.League(league_object)

print(lcs)
print(lcs.listTournaments())