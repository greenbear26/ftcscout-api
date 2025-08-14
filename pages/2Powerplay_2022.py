import streamlit
import sys
import pandas

import request
import utils.general as general
import utils.predoubleelim as predoubleelim

def countAwards(teams):
    general.countAwards(teams)

def countRanking(teams):
    general.countRanking(teams)

def countAdvancement(teams):
    predoubleelim.countAdvancement(teams)

def countAlliance(teams):
    predoubleelim.countAlliance(teams)

def main():
    manual = "https://www.firstinspires.org/resource-library/ftc/game-and-season-info"
    streamlit.title(":green[FTC 2022: Powerplay] Advancement Points Calculator")
    streamlit.write("This program will calculate the points that teams at a\
                    given competition would get using the 2025 points ranking\
                    system. The calculation follows the\
                    specifics detailed in the 2025 [competition manual](%s), \
                    with these small tweaks:" % manual)
    streamlit.write("- Both semifinalist alliances will receive 10 points,\
                    because there is no way to distinguish between 3rd and 4th\
                    place.") 
    streamlit.write("- 2nd picks of alliances will get 4 points less than\
                    captains and first picks.")

    event_code = streamlit.text_input("Event Code")
    try:
        teams = request.getTeamsFromEvent(event_code, 2022)
    except:
        ftc_events = "https://ftc-events.firstinspires.org/2022#allevents"
        streamlit.write("Event code not valid. Refer to [FTCEvents](%s) for valid\
                        event codes." % ftc_events)
        return
    
    countAwards(teams)
    countRanking(teams)
    countAdvancement(teams)
    countAlliance(teams)

    teams.sort(key=lambda team: team["points"], reverse=True)

    dataframe = pandas.DataFrame({
        "Team Number": [team["teamNumber"] for team in teams],
        "Team Name": [team["team"]["name"] for team in teams],
        "Points": [team["points"] for team in teams]
    })

    streamlit.dataframe(dataframe, hide_index=True)

    streamlit.write("###### Created by Rishi Ponnapalli")


if __name__ == "__main__":
    main()
