
from google.cloud import storage

class blob_test:
    def __init__(self, s_client, b_name):
        self.storage_client = s_client
        self.bucket_name = b_name

    def get_bucket(self):
        storage_client = self.storage_client
        bucket_name = self.bucket_name
        bucket = storage_client.get_bucket(bucket_name)
        return bucket

    def list_blobs(self):
        storage_client = self.storage_client
        bucket_name = self.bucket_name
        """
        list_blobs 
        return : iterator of all blobs in the bucket
        """
        blobs_iter = storage_client.list_blobs(bucket_name)
        return blobs_iter

if __name__ == '__main__':

    BUCKET_NAME = 'hello_test_bucket_1208'
    storage_client = storage.Client()

    b = blob_test(storage_client, BUCKET_NAME)
    blobs = b.list_blobs()
    for num, blob in enumerate(blobs, 1):
        name = blob.name
        type = blob.content_type
        bucket = blob.bucket
        size = blob.size
        print(f"""
        [ blob{num} ]
        name : {name}
        type : {type}
        bucket : {bucket}
        size : {size} B
        """)
