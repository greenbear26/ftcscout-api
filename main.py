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

def countAdvancement(teams):
    for team in teams:
        matches = team["matches"]
        if (matches):
            # Checking if they played in a match
            played = False
            for match in matches:
                if match["onField"]:
                    played = True
                    break
            
            if played:
                final_match = matches[len(matches)-1]["match"]["description"]
                final_match_number = int(final_match[2:])
                if final_match_number == 12:
                    team["points"] += 5
                elif final_match_number == 13:
                    team["points"] += 10
                elif final_match_number >= 14:
                    for award in team["awards"]:
                        if award["type"] == "Finalist":
                            team["points"] += 20
                        elif award["type"] == "Winner":
                            team["points"] += 40

def main():
    teams = request.getTeamsFromEvent("FTCCMP1FRAN")
    
    countAwards(teams)
    countRanking(teams)
    countAdvancement(teams)

    teams.sort(key=lambda team: team["points"], reverse=True)
    for team in teams:
        print(str(team["teamNumber"]) + ": " + str(team["points"]))


if __name__ == "__main__":
    main()
