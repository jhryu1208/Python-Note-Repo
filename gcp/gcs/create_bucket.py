from google.cloud import storage

storage_client = storage.Client()

"""
create bucket
"""
BUCKET_NAME = 'hello_test_bucket_1208'
LOCATION = 'asia-northeast3'
CLASS = 'STANDARD' # STANDARD, COLDLINE, ARLINE, ARCHIVE

bucket = storage_client.bucket(BUCKET_NAME) # create bucket object
bucket.location = LOCATION
bucket.storage_class = CLASS

print(f"""
bucket name : {bucket.name}\n
bucket location : {bucket.location}\n
bucket class : {bucket.storage_class}
""")

# pass the resource object to the client
# return newly create bucket
bucket = storage_client.create_bucket(bucket)
