from bs4 import BeautifulSoup
import requests
import json
import cloudscraper
import pandas as pd
data=[]
newdata=[]

goals=[]
assists=[]
name=[]
country=[]
club=[]
position=[]
url = "https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v2/competitions/8/seasons/2024/players/stats/leaderboard?_sort=goals%3Adesc&_limit=10"
for i in range (0,25):
    scraper = cloudscraper.create_scraper()

    response = scraper.get(url)
    data1 = response.json()
    next_token = data1["pagination"]["_next"]
    
    for j in range (0,10):
        goals.append(data1['data'][j]['stats']['goals'])
        assists.append(data1['data'][j]['stats'].get('goalAssists',0))
        name.append(data1['data'][j]['playerMetadata']['name'])
        country.append(data1['data'][j]['playerMetadata']['country']['country'])
        club.append(data1['data'][j]['playerMetadata']['currentTeam']['name'])
        position.append(data1['data'][j]['playerMetadata']['position'])


    url="https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v2/competitions/8/seasons/2024/players/stats/leaderboard?_sort=goals%3Adesc&_limit=10&_next=" + next_token

    
matrix=[]
for i in range(250):
    row = [name[i], club[i],assists[i], goals[i],position[i]]
    matrix.append(row)

# Print the matrix
df = pd.DataFrame(matrix)