
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as BS
import warnings
import json

warnings.filterwarnings('ignore')

# making sure we can see the whole table
desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 25)

# example of pulling stats for Lamar Jackson from his gamelog page on ESPN
res = requests.get('https://site.web.api.espn.com/apis/common/v3/sports/football/nfl/athletes/3916387/gamelog')
content = json.loads(res.content)

print(content)
print(content['seasonTypes'][0])

for key in content['seasonTypes']:
    print(key)


# http://api.espn.com/v1/sports/baseball/mlb/athletes/3748
# /{version}/sports/{sport}/{league}/athletes/{athleteID}


if res.ok:
    data = res.json() #converting response from API to json response (list)

    #not sure I need df_values, but in video
    # df_values = {
    #     'player_name': [],
    #     'pos': [],
    #     'team': [],
    #     'projection': []
    # }
    #print(data)
    df = pd.DataFrame(content['seasonTypes'])

    #separate dataframes for each position
    # qb_df = df[df['pos'] == 'QB']
    # rb_df = df[df['pos'] == 'RB']
    # wr_df = df[df['pos'] == 'WR']
    # te_df = df[df['pos'] == 'TE']

    #saving all projectsions to file (doubt need)
    #df.to_csv('data/projections.csv')

## ISSUE: need to pull the right dictionary key from the JSON file for the stats
print(df.head())

