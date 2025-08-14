from scipy.special import erfinv
import math

def countAwards(teams):
    for team in teams:
        awards = team["awards"]
        if (awards):
            for award in awards:
                if award["type"] == "Winner" or award["type"] == "Finalist" or \
                award["type"] == "DeansListFinalist":
                    continue
                elif award["type"] == "Inspire":
                    team["points"] += (2**(3 - award["placement"]) * 15)
                else:
                    team["points"] += (2**(3 - award["placement"]) * 3)

def countRanking(teams):
    for team in teams:

        n = len(teams)
        r = team["stats"]["rank"]
        alpha = 1.07

        # Standard formala given by competition manual
        qual_points = erfinv((n - 2*r + 2) / (alpha*n)) * 7 / erfinv(1 / alpha) + 9

        team["points"] += round(qual_points)
