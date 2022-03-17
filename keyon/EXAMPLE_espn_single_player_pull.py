import requests
import pandas as pd
import numpy as np
# from bs4 import BeautifulSoup as BS
import warnings
import json

warnings.filterwarnings('ignore')

# making sure we can see the whole table
desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 25)

# example of pulling stats for Lamar Jackson from his gamelog page on ESPN
athlete_url = 'https://site.web.api.espn.com/apis/common/v3/sports/football/nfl/athletes/{athlete_id}/gamelog'
athlete_list = [15818, 3916387] # list of potential athletes first one is Keenan Allen, next is Lamar Jackson

for athlete_id in athlete_list:
    access_url = athlete_url.format(athlete_id=athlete_id)
    res = requests.get(access_url)

    if res.ok:
        data = res.json() # converting response from API to json response (list)

        df_nested_list = pd.json_normalize(data['seasonTypes'], record_path =['categories'])     # cleans up JSON data down to category level where data is
        df1 = pd.DataFrame(df_nested_list['events'])        # goes one level down into 'events', which gives us a list of dictionaries again
        df1_tolist = df1['events'].tolist()         # since it is a list of dictionaries inside a df, have to make it an actual list
        df2 = pd.DataFrame(df1_tolist[0])           # take the list and turn back into a df
        df_stats = pd.DataFrame(df2['stats'].to_list(), columns=data['displayNames'])
        event_column = df2['eventId']               # need to add the events back in, so making it a list to add

        df_final = pd.concat([df_stats, event_column], axis=1)

        df_final['athlete_id'] = athlete_id         # add id f
        event_column = df_final.pop('eventId')  # moving the event column to front
        df_final.insert(0, 'eventId', event_column)
        print(df_final)
        # df_final.to_csv('df_final.csv')     # saving to csv for fun

