# Football Import
from espn_api.football import League
import requests
import pandas as pd
import numpy as np
import warnings
import json
from google.cloud import bigquery

# EXAMPLE of using the python version of ESPN v3 for importing a league

# making sure we can see the whole table
desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 25)

# K's personal cookie info
s2 = "AECAlZGGZ%2BKVVazn84JPRPKlzGn8c0h0mgcW%2BmMD7rZbRi7Eo%2FD0AftzOhmp%2Bp2OXGN4jU37nau7amjPktismejCclO5Nw2itHBLxlMp5ho0TL9dQYfP8ElaaVYyi8r1rL5VfDEz9ZvVDKtNE2kqhfi5yeNP5G4H75oQV7I6j4oIqUTPdvXSW6KExsDka6tNgzr5Nlrbo1VLR2v7wqsUwnPHjL2y930EX9xhSzVCvN7Nhq47eb%2B%2FTed93BQHkkt1zSj0pk6BF0cQZVSWymyq5%2BSV"
sw_id = "{D3FB8C91-2170-4F49-9BF1-CFF8AABC99A1}"

# initialize bigquery
client = bigquery.Client()
table_id = "funky-fantasy-hosting-1.ff_league_table.league_{id}"


# Alternate examples
# public league
# league = League(league_id=1245, year=2018)
# private league with username and password
# league = League(league_id=1245, year=2018, username='userName', password='pass')
# debug mode
# league = League(league_id=1245, year=2018, debug=True)



# LEAGUE TYPES: 0 - Guillotine 1 - Vampire 2 - Pirate
# lid = 1151092
def pull_new_league(lid, l_type=0):
    # hard code example for testing (private league)
    # league = League(league_id=1151092, year=2019, espn_s2=s2, swid=sw_id, debug=True)
    league = League(league_id=lid, year=2022)
    df_league = pd.DataFrame(columns=['league_id', 'team_id', 'team_name', 'league_type', 'user_ids',
                                      'score_settings', 'league_size', 'league_commish'])


    # row for every team, right now assumption commish is first team
    for team in league.teams:  # loop to create dictionary
        df_league = df_league.append({'league_id': lid, 'team_id': team.team_id, 'team_name': team.team_name,
                                      'league_type': l_type,
                                      'league_size': len(league.teams),
                                      'league_commish': (1 if team.team_id == 1 else 0)}, ignore_index=True)


    # changing from float to int
    df_league.league_id = df_league.league_id.astype(int)
    df_league.league_type = df_league.league_type.astype(int)
    df_league.league_size = df_league.league_size.astype(int)

    print(df_league)

    # saving to the bigquery table
    job = client.load_table_from_dataframe(
        df_league, table_id.format(id=lid),
    )  # Make an API request.
    job.result()  # Wait for the job to complete.

    table = client.get_table(table_id.format(id=lid))  # Make an API request.
    print(
        "Loaded {} rows and {} columns to {}".format(
            table.num_rows, len(table.schema), table_id.format(id=lid)))

    return df_league




# pull_new_league(1151092, 2)


# example of pulling a player
# lamar_jackson = league.player_info(playerId=3916387)

# example of pulling free agents
# league.free_agents(week=3)