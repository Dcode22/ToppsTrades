import requests
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trading_cards.settings')
django.setup()
from tradingpost.models import Card, Team

url = "https://rapidapi.p.rapidapi.com/json/named.team_all_season.bam"

querystring = {"season":"'2020'","all_star_sw":"'N'","sort_order":"name_asc"}

headers = {
    'x-rapidapi-host': "mlb-data.p.rapidapi.com",
    'x-rapidapi-key': "345fb3df58msh72ac91b479fe33dp1908c3jsnd24d180fc16b"
    }

response = requests.request("GET", url, headers=headers, params=querystring)



data = response.json()["team_all_season"]["queryResults"]["row"]

for team in data:
    team_id= team['team_id']
    # if Team.objects.filter(mlb_id=team_id).exists():
    #     answer= input("a team of this name already exists, would you like to skip? y/n")
    #     if answer== "y":
    #         continue
    url = "http://lookup-service-prod.mlb.com/json/named.roster_40.bam"
    querystring= {
        "team_id": team_id
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()["roster_40"]["queryResults"]["row"]
    for player_dict in data:
        team, created = Team.objects.get_or_create(mlb_id= player_dict['team_id'], name= player_dict['team_name'])
        if Card.objects.filter(player_id= player_dict["player_id"]).exists():
            continue
        card= Card.objects.create(name= player_dict['name_display_first_last'], 
        position= player_dict['position_txt'],
        weight= player_dict['weight'],
        height_ft= player_dict['height_feet'],
        height_in= player_dict['height_inches'],
        jersey_number= player_dict['jersey_number'],
        bats= player_dict['bats'],
        throws= player_dict['throws'],
        birth_date= player_dict['birth_date'],
        team= team,
        player_id= player_dict['player_id']
        )
        print(card)
        
