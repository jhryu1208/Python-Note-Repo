# pip install --upgrade google-cloud-bigquery
from google.cloud import bigquery

"""
C : create_dataset
R : get_dataset (or bigquery.DatasetReference)
U : update_dataset
D : delete_datset
"""

bq_client = bigquery.Client()
project_id = 'jihyun-gcp01'

"""
[ dataset / DatasetReference ]

dataset
- Deprecated since version 1.24.0: Construct a DatasetReference using its constructor
- return : DatasetReference instance
- return type : google.cloud.bigquery.dataset.DatasetReference
- "get_dataset" that is method for bigquery client returns same type

DatasetReference
- param
    - project
    - dataset_id
- raise : ValueError

"""

dataset_instance1 = bigquery.Dataset(f'{project_id}.test_project1')
dataset_instance2 = bigquery.DatasetReference(project_id, 'test_project1')
# get_dataset도 bigquery의 Dataset 메소드와 동일한 class객체를 반환하지만,
# get_dataset의 경우 dataset이 존재하지 않을 경우 error를 raise한다.
# 따라서, create하기도 전에 해당 메소드는 사용할 수 없다.
dataset_instance3 = bq_client.get_dataset(f'{project_id}.test_project1')


print(dataset_instance1, type(dataset_instance1))
# Dataset(DatasetReference('project_id', 'test_project1'))
# <class 'google.cloud.bigquery.dataset.Dataset'>
print(dataset_instance2, type(dataset_instance2))
# DatasetReference('project_id', 'test_project1')
# <class 'google.cloud.bigquery.dataset.DatasetReference'>
print(dataset_instance3, type(dataset_instance3))
# Dataset(DatasetReference('project_id', 'test_project1'))
# <class 'google.cloud.bigquery.dataset.Dataset'>

print(dataset_instance2.dataset_id) # print out dataset_id
print(dataset_instance2.path) # print out URL path for the dataset based on project and dataset ID (Ex. /project/[Project_ID]/datasets/[Dataset_ID])
print(dataset_instance2.project) # print out project_id


"""
[ create_dataset ]
- param
    - dataset
    - exists_ok : (default=false). if true, ignore "already exists" errors when createing the dataset
- return : A new dataset returned from the api
- raises: google.cloud.exceptions.Conflict - if the dataset already exists
"""

dataset = bigquery.DatasetReference(project_id, 'test_project2')
dataset = bq_client.create_dataset(dataset, exists_ok = True)
print(f"""
project_id : {dataset.project}
dataset_id : {dataset.dataset_id}
""")

"""
[ delete_datset ]
- param
    - dataset
    - delete_contents
        - True, delete all the tables in the dataset
        - If False and the dataset contains tables, the request will fail.
          : 데이터셋 내부에 테이블이 존재하고 해당 param이 False일 경우 에러가 raise됨
        - Default is False.
    - not_found_ok
        - Default False
        - True : ignore "not found" errors when deleting the dataset
- return : None
"""

dataset = bq_client.get_dataset(f'{project_id}.test_project2')
dataset = bq_client.delete_dataset(dataset, not_found_ok = True)
print(dataset, type(dataset)) # None <class 'NoneType'>

"""
[ update_dataset ]
- param
    - dataset (Class : google.cloud.bigquery.dataset.Dataset)
    - fields
"""

dataset = bq_client.get_dataset(f'{project_id}.test_project1')
dataset.description = 'Update Dataset'
dataset.default_table_expiration_ms  = 24*60*60*100 # In milliseconds.

dataset = bq_client.update_dataset(dataset, ["description", "default_table_expiration_ms"])
