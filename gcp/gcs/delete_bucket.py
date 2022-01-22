
from google.cloud import storage

storage_client = storage.Client()

"""
create bucket
"""

BUCKET_NAME = 'byebyebucket-20220123'
LOCATION = 'asia-northeast3'
CLASS = 'STANDARD' # STANDARD, COLDLINE, ARLINE, ARCHIVE

bucket = storage_client.bucket(BUCKET_NAME)
bucket.location = LOCATION
bucket.storage_class = CLASS

create_bucket = storage_client.create_bucket(BUCKET_NAME)

"""
check for created bucket
"""

bucket_iter = storage_client.list_buckets()
bucket_list = [bucket for bucket.name in bucket_iter]

try:
    BUCKET_NAME in bucket_list
    print(f'check : {BUCKET_NAME}')
except ValueError:
    print('bucket is not shown')


"""
delete bucket
"""

create_bucket.delete()

print("Bucket {} deleted".format(bucket.name))
