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

def main():
    teams = request.getTeamsFromEvent("FTCCMP1FRAN")
    
    countAwards(teams)

    for team in teams:
        print(str(team["teamNumber"]) + ": " + str(team["points"]))


if __name__ == "__main__":
    main()
