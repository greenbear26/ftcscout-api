import sys
import math
import request
import eightalliance
import sixalliance
import fouralliance
import twoalliance

def countAwards(teams):
    for team in teams:
        awards = team["awards"]
        if (awards):
            for award in awards:
                if award["type"] == "Winner" or award["type"] == "Finalist":
                    continue
                elif award["type"] == "Inspire":
                    team["points"] += (2**(3 - award["placement"]) * 15)
                else:
                    team["points"] += (2**(3 - award["placement"]) * 3)

def countRanking(teams):
    step = 14 / (len(teams) - 1)
    for team in teams:
        inverted_rank = (len(teams) - team["stats"]["rank"])
        team["points"] += math.floor(inverted_rank * step) + 2

def countAdvancement(teams):
    if len(teams) > 40:
        eightalliance.countAdvancement(teams)
    elif len(teams) > 20:
        sixalliance.countAdvancement(teams)
    elif len(teams) > 10:
        fouralliance.countAdvancement(teams)
    else:
        twoalliance.countAdvancement(teams)

def countAlliance(teams):
    if len(teams) > 40:
        eightalliance.countAlliance(teams)
    elif len(teams) > 20:
        sixalliance.countAlliance(teams)
    elif len(teams) > 10:
        fouralliance.countAlliance(teams)
    else:
        twoalliance.countAlliance(teams)


def main():
    if len(sys.argv) > 1:
        teams = request.getTeamsFromEvent(sys.argv[1])
    else:
        print("Please provide an event code")
        return
    
    countAwards(teams)
    countRanking(teams)
    countAdvancement(teams)
    countAlliance(teams)

    teams.sort(key=lambda team: team["points"], reverse=True)
    for team in teams:
        print(str(team["teamNumber"]) + ": " + str(team["points"]))


if __name__ == "__main__":
    main()
