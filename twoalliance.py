def countAdvancement(teams):
    for team in teams:
        for award in team["awards"]:
            if award["type"] == "Finalist":
                team["points"] += 20
            elif award["type"] == "Winner":
                team["points"] += 40

def countAlliance(teams):
    for team in teams:
        matches = team["matches"]
        if matches:
            match_color = matches[0]["alliance"]

            alliance_number = 0

            if match_color == "Red":
                alliance_number = 1
            else:
                alliance_number = 2

            team["points"] += 21 - alliance_number
