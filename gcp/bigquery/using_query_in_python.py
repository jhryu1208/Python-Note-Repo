from google.cloud import bigquery

sql = """
SELECT 1
"""

bq_client = bigquery.Client()
return1 = bq_client.query(sql)
df = return1.to_dataframe()
print(df)
