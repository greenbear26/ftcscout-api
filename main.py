import math
import request

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

def main():
    teams = request.getTeamsFromEvent("FTCCMP1FRAN")
    
    countAwards(teams)
    countRanking(teams)

    teams.sort(key=lambda team: team["points"], reverse=True)
    for team in teams:
        print(str(team["teamNumber"]) + ": " + str(team["points"]))


if __name__ == "__main__":
    main()
