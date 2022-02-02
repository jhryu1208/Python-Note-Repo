
"""
[ load_table_from_dataframe ]
- Upload the contents of a table from a pandas DataFrame.
- param
    - dataframe : A DataFrame containing the data to load.
    - destination
        - The destination table to use for loading the data.
        - If it is an existing table, the schema of the DataFrame must match the schema of the destination table.
        - If the table does not yet exist, the schema is inferred from the DataFrame.

[ load_table_from_file ]
- Upload the contents of this table from a file-like object.
- param
    - file_obj : "A file handle" opened in binary mode for reading.
    - destination

[ load_table_from_json ]
- Upload the contents of a table from a JSON string or dict.
- param
    - json_rows
        - Row data to be inserted
        - Keys must match the table schema fields and values must be JSON-compatible representations.
    - destination

[ load_table_from_uri ]
- Starts a job for loading data into a table from Cloud Storage.
- param
    - source_uris
        - URIs of data files to be loaded
        - gs://<bucket_name>/<object_name_or_glob>
    - destination
"""
from google.cloud import storage, bigquery
import pandas as pd
import json
import io
import os

def from_dataframe(df, dest):
    client = bigquery.Client()
    job_config = bigquery.LoadJobConfig(autodetect=True, write_disposition = 'WRITE_TRUNCATE')
    load_job = client.load_table_from_dataframe(df, dest, job_config = job_config)
    load_job.result()

def from_file(file_path, dest):
    client = bigquery.Client()
    job_config = bigquery.LoadJobConfig(source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1, autodetect=True, write_disposition = 'WRITE_TRUNCATE') # load_job 설정
    with open(file_path, 'rb') as f:
        load_job = client.load_table_from_file(f, dest, job_config=job_config)
        load_job.result()

def from_json(json_path, dest):
    client = bigquery.Client()
    job_config = bigquery.LoadJobConfig(autodetect=True, write_disposition = 'WRITE_TRUNCATE')
    with open(json_path, 'rb') as f:
        json_data = json.load(f)
        first_key = list(json_data.keys())[0]
        load_job = client.load_table_from_json(json_data[first_key], dest, job_config = job_config)
        load_job.result()

def from_uris(uri, dest):
    client = bigquery.Client()
    job_config = bigquery.LoadJobConfig(autodetect=True, write_disposition = 'WRITE_TRUNCATE')
    load_job = client.load_table_from_uri(uri, dest, job_config = job_config)
    load_job.result()

if __name__ == '__main__':

    project_path = os.getcwd()
    project_id = 'jihyun-gcp01'
    dataset_id = 'test_project2'

    file_path = project_path+'\\gcp\\test_file\\tottenham.csv'
    json_path = project_path+'\\gcp\\test_file\\tottenham.json'
    uri = 'gs://hello_test_bucket_1208/tottenham.csv'
    df = pd.read_csv(file_path, sep = ',', encoding='utf-8')
    df = df[['name', 'age','height', 'place_of_bith', 'main_position']]

    dest_table_df = f'{project_id}.{dataset_id}.from_df'
    dest_table_file = f'{project_id}.{dataset_id}.from_file'
    dest_table_json = f'{project_id}.{dataset_id}.from_json'
    dest_table_uri = f'{project_id}.{dataset_id}.from_uri'

    def main():
        from_dataframe(df, dest_table_df)
        from_json(json_path, dest_table_json)
        from_file(file_path, dest_table_file)
        from_uris(uri, dest_table_uri)

    main()
