import requests

def getTeamsFromEvent(eventCode):
    url = "https://api.ftcscout.org/graphql"

    query = """
        query Query($season: Int!, $code: String!) {
          eventByCode(season: $season, code: $code) {
            teams {
              teamNumber
              stats {
                ... on TeamEventStats2024 {
                  rank
                }
              }
              awards {
                type
                placement
              }
              matches {
                match {
                  description
                }
                alliance
                onField
                allianceRole
              }
            }
          }
        }
    """

    variables = {
      "season": 2024,
      "code": eventCode
    }

# Data to be sent in the request body
    payload = {
        "query": query,
        "variables": variables
    }

    data = None
    try:
        # Make the POST request with JSON data
        response = requests.post(url, json=payload)

        # Check if the request was successful (status code 201 Created)
        if response.status_code == 200:
            data = response.json()
            print("POST Request Successful:")
        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    teams = data["data"]["eventByCode"]["teams"]

    # Removing empty teams
    teams = [team for team in teams if team["stats"]]

# Removing unnecessary matches
    for team in teams:
        matches = team["matches"]
        # Filter out non-"M" matches
        team["matches"] = [match for match in matches 
                          if match["match"]["description"][0] == "M"]

        # Adding poitns attribute to every team
        team["points"] = 0

    return teams
