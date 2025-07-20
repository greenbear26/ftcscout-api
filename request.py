import requests

url = "https://api.ftcscout.org/graphql"

query = """
    query ExampleQuery($number: Int!) {
      teamByNumber(number: $number) {
        name
        rookieYear
        location {
            country
            state
            city
        }
        schoolName
      }
    }
"""

variables = {
    "number": 19411
}

# Data to be sent in the request body
payload = {
    "query": query,
    "variables": variables
}

try:
    # Make the POST request with JSON data
    response = requests.post(url, json=payload)

    # Check if the request was successful (status code 201 Created)
    if response.status_code == 200:
        data = response.json()
        print("POST Request Successful:")
        print(data)
    else:
        print(f"Error: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
