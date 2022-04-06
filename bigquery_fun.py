from google.cloud import bigquery
from google.cloud.exceptions import NotFound

client = bigquery.Client()

# TODO(developer): Set dataset_id to the ID of the dataset to determine existence.
dataset_id = "funky-fantasy-hosting-1.ff_league_table"

# try:
#     client.get_dataset(dataset_id)  # Make an API request.
#     print("Dataset {} already exists".format(dataset_id))
# except NotFound:
#     print("Dataset {} is not found".format(dataset_id))

# def queryTbl(sql):
#     client.get_dataset(dataset_id)
#     query = client.query(sql)
#     print(query)
#     #results = query.result()
#     #print(results.to_dataframe)

# qry = "SELECT * FROM funky-fantasy-hosting-1.ff_league_table"

# queryTbl(qry)

sql = """
    SELECT *
    FROM `funky-fantasy-hosting-1.ff_league_table.league_721301807`
    WHERE team_id = 1
"""

df = client.query(sql).to_dataframe()
print(df)