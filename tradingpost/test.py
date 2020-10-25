import requests
import random

url = "https://rapidapi.p.rapidapi.com/json/named.player_info.bam"
id = f"'{random.randint(300000, 500000)}'"
print(id)
q= {
    "sport_code":"'mlb'",
    "player_id": id
}
querystring = q
headers = {
    'x-rapidapi-host': "mlb-data.p.rapidapi.com",
    'x-rapidapi-key': "345fb3df58msh72ac91b479fe33dp1908c3jsnd24d180fc16b"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)