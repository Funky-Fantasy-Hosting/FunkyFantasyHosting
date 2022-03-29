from google.cloud import bigquery
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


bqclient = bigquery.Client()

# Download query results.
query_string = """
SELECT *
FROM `funky-fantasy-hosting-1.player_gamelogs_pivot.nfl_player_bio`

"""

dataframe = (
    bqclient.query(query_string)
    .result()
    .to_dataframe(
        # Optionally, explicitly request to use the BigQuery Storage API. As of
        # google-cloud-bigquery version 1.26.0 and above, the BigQuery Storage
        # API is used by default.
        create_bqstorage_client=True,
    )
)
print(dataframe.head())