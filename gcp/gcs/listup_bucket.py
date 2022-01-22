
from google.cloud import storage

storage_client = storage.Client()

bucket_list = storage_client.list_buckets()
print(type(bucket_list)) # HTTPIterator

for num, bucket in enumerate(bucket_list, 1):
    print(type(bucket))
    print(
    f"""
    [ bucket info{num} ]
    name : {bucket.name}
    location : {bucket.location}
    class : {bucket.storage_class}
    """
    )
