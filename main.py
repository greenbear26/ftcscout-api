import streamlit
import sys
import math
import pandas
from scipy.special import erfinv

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
    # step = 14 / (len(teams) - 1)
    for team in teams:
        # inverted_rank = (len(teams) - team["stats"]["rank"])
        # team["points"] += math.floor(inverted_rank * step) + 2

        n = len(teams)
        r = team["stats"]["rank"]
        alpha = 1.07

        # Standard formala given by competition manual
        qual_points = erfinv((n - 2*r + 2) / (alpha*n)) * 7 / erfinv(1 / alpha) + 9

        team["points"] += math.floor(qual_points)

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
    manual = "https://www.firstinspires.org/resource-library/ftc/game-and-season-info"
    streamlit.title(":blue[FTC 2024: Into the Deep] Advancement Points Calculator")
    streamlit.write("This program will calculate the points that teams at a\
                    given competition would get using the 2025 points ranking\
                    system. For the most part, the calculation follows the\
                    calculation detailed in the 2025 [competition manual](%s), with\
                    some exceptions regarding alliances at worlds." % manual)

    # if len(sys.argv) > 1:
    event_code = streamlit.text_input("Event Code")
    try:
        teams = request.getTeamsFromEvent(event_code)
    except:
        ftc_events = "https://ftc-events.firstinspires.org/2024#allevents"
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
        "Points": [team["points"] for team in teams]
    })

    streamlit.dataframe(dataframe, hide_index=True)

    streamlit.write("###### Created by Rishi Ponnapalli")


if __name__ == "__main__":
    main()
