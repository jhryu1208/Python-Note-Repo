from google.cloud import bigquery

# construct a bigquery client object
client = bigquery.Client()
project_id = 'jihyun-gcp01'
dataset_id = 'test_project1'

"""
C : create_table, copy_table
R : get_table (or bigquery.Table)
D : delete_table
"""

"""
[ create_table ]
- param
    - table
    - exists_ok : Defaults to False. If True, ignore “already exists” errors when creating the table.

참고) External Data Source를 통해서 Table을 생성할 수 있음
- Bigtable
- Cloud Spanner
- Cloud SQL
- Cloud Storage
- Drive
"""

# Creating an empty table with a schema definition
schema = [
    bigquery.SchemaField("name", "STRING", mode = "REQUIRED"),
    bigquery.SchemaField("sex", "STRING", mode = "REQUIRED"),
    bigquery.SchemaField("email", "STRING", mode = "NULLABLE"),
]

table = bigquery.Table(f'{project_id}.{dataset_id}.create_table1', schema = schema)
table = client.create_table(table, exists_ok=True) # make an api request
print(f"""
project_id : {table.project}
dataset_id : {table.dataset_id}
table_id : {table.table_id}
""")


# Creating a table from a query result
sql = f"""
CREATE OR REPLACE TABLE {project_id}.{dataset_id}.create_table2
AS
(
    SELECT corpus
    FROM `bigquery-public-data.samples.shakespeare`
    GROUP BY corpus
)
"""

query_job = client.query(sql)  # Make an API request.


"""
[ get_table ]
- param
    - table
- return : table instance
- type : google.cloud.bigquery.table.Table

[ list_tables ]
- param
    - dataset
    - max_results : Maximum number of tables to return. Defaults to a value set by the API.
- Returns : Iterator of TableListItem contained within the requested dataset.

[ list_rows ]
- param
    - table
    - selected_fields : The fields to return. If not supplied, data for all columns are downloaded.
    - max_results : Maximum number of rows to return.
- returns
    - Iterator of row data Row-s
    - the iterator will have the total_rows attribute
    - RowIterator를 반환하기 때문에 to_dataframe메소드 적용 가능
"""

dataset = client.get_dataset(f'{project_id}.{dataset_id}')
table_list = client.list_tables(dataset)
print([i.table_id for i in table_list]) # get table_id from TableListItem

table = client.get_table(f'{project_id}.{dataset_id}.create_table1')
print(f"""
project_id : {table.project}
dataset_id : {table.dataset_id}
table_id : {table.table_id}
""")

table_rows = client.list_rows(table)
df = table_rows.to_dataframe() # RowIterator to DataFrame
print(df.head(5))

"""
[ delete_table ]
- param
    - table
    - not_found_ok : Defaults to False. If True, ignore “not found” errors when deleting the table.
"""

table = client.get_table(f'{project_id}.{dataset_id}.create_table1')
client.delete_table(table, not_found_ok = True)

"""
[ copy_table ]
- param
    - sources : Table or tables to be copied.
    - destination : Table into which data is to be copied.

- Returns: A new copy job instance.
- Return type: google.cloud.bigquery.job.CopyJob
"""

sql = \
f"""
CREATE OR REPLACE TABLE `{project_id}.{dataset_id}.source_table1`
AS
(
    SELECT corpus
    FROM `bigquery-public-data.samples.shakespeare`
    GROUP BY corpus
    LIMIT 10
);

CREATE OR REPLACE TABLE  `{project_id}.{dataset_id}.source_table2`
AS
(
    SELECT corpus
    FROM `bigquery-public-data.samples.shakespeare`
    GROUP BY corpus
    LIMIT 10 OFFSET 11
);
"""

query = client.query(sql) # create_query
query.result()

# create source table class object
source_table1 = client.get_table(f'{project_id}.{dataset_id}.source_table1')
source_table2 = client.get_table(f'{project_id}.{dataset_id}.source_table2')

# create destination table class object
dest_table1 = bigquery.Table(f'{project_id}.{dataset_id}.dest_table1')
dest_table2 = bigquery.Table(f'{project_id}.{dataset_id}.dest_table2')

# only one table copy
client.copy_table([source_table1], dest_table1)
# multi table copy (operating like "union all")
client.copy_table([source_table1, source_table2], dest_table2)
