from google.cloud import bigquery, storage

# construct a bigquery client object
bq_client = bigquery.Client()
gcs_client = storage.Client()
project_id = 'jihyun-gcp01'
dataset_id = 'test_project1'
BUCKET_NAME = 'test_extracting'

"""
[ extract_table ]
- param
    - source(single/multi(union))
    - destination_uris(single/multi(union))
      : URIs of Cloud Storage file(s) into which table data is to be extracted;
        in format gs://<bucket_name>/<object_name_or_glob>.
- Returns : A new extract job instance.
"""

#bucket = gcs_client.bucket(BUCKET_NAME)
#bucket = gcs_client.create_bucket(bucket)

source_table1 = bq_client.get_table(f'{project_id}.{dataset_id}.source_table1')
source_table2 = bq_client.get_table(f'{project_id}.{dataset_id}.source_table2')

dest_path1 = f'gs://{BUCKET_NAME}/dest_path1.csv'
dest_path2 = f'gs://{BUCKET_NAME}/dest_*.csv' # partitioned

extract_job1 = bq_client.extract_table(source_table1, [dest_path1])
extract_job1.result()

extract_job2 = bq_client.extract_table(source_table2, [dest_path2])
extract_job2.result()
