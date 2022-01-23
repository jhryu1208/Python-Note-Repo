
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

        print(f"""
        [ blob{num} ]
        name: {blob.name}
        type: {blob.content_type}
        bucket: {blob.bucket}
        size: {blob.size} B
        """)

"""
    print("Blob: {}".format(blob.name))
    print("Bucket: {}".format(blob.bucket.name))
    print("Storage class: {}".format(blob.storage_class))
    print("ID: {}".format(blob.id))
    print("Size: {} bytes".format(blob.size))
    print("Updated: {}".format(blob.updated))
    print("Generation: {}".format(blob.generation))
    print("Metageneration: {}".format(blob.metageneration))
    print("Etag: {}".format(blob.etag))
    print("Owner: {}".format(blob.owner))
    print("Component count: {}".format(blob.component_count))
    print("Crc32c: {}".format(blob.crc32c))
    print("md5_hash: {}".format(blob.md5_hash))
    print("Cache-control: {}".format(blob.cache_control))
    print("Content-type: {}".format(blob.content_type))
    print("Content-disposition: {}".format(blob.content_disposition))
    print("Content-encoding: {}".format(blob.content_encoding))
    print("Content-language: {}".format(blob.content_language))
    print("Metadata: {}".format(blob.metadata))
    print("Custom Time: {}".format(blob.custom_time))
    print("Temporary hold: ", "enabled" if blob.temporary_hold else "disabled")
    print(
        "Event based hold: ",
        "enabled" if blob.event_based_hold else "disabled",
    )
    if blob.retention_expiration_time:
        print(
            "retentionExpirationTime: {}".format(
                blob.retention_expiration_time
            )
        )
"""
