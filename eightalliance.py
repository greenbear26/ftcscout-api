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

def countAlliance(teams):
    for team in teams:
        matches = team["matches"]
        if matches:
            first_match = matches[0]["match"]["description"]
            first_match_number = int(first_match[2:])
            match_color = matches[0]["alliance"]

            alliance_number = 0

            if (first_match_number == 1):
                if match_color == "Red":
                    alliance_number = 1
                else:
                    alliance_number = 8
            elif (first_match_number == 2):
                if match_color == "Red":
                    alliance_number = 4
                else:
                    alliance_number = 5
            elif (first_match_number == 3):
                if match_color == "Red":
                    alliance_number = 2
                else:
                    alliance_number = 7
            elif (first_match_number == 4):
                if match_color == "Red":
                    alliance_number = 3
                else:
                    alliance_number = 6

            # Compensating for snake draft format
            if matches[0]["allianceRole"] == "SecondPick":
                alliance_number = 17 - alliance_number

            team["points"] += 21 - alliance_number
