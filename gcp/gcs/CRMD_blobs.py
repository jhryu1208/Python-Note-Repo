
from google.cloud import storage

class blob_test:
    def __init__(self, s_client, b_name):
        self.bucket_name = b_name
        self.storage_client = s_client

    """
    rename
    """
    def rename_blob(self, target_blob_name, new_name):

        storage_client = self.storage_client
        bucket_name = self.bucket_name

        bucket = storage_client.bucket(bucket_name)
        target_blob = bucket.blob(target_blob_name)

        new_blob = bucket.rename_blob(target_blob, new_name) # change blob name

        print(f"Blob {target_blob.name} has been renamed to {new_blob.name}")

    """
    copy
    """
    def copy_blob(self, target_blob_name, destination_bucket_name, destination_blob_name):

        storage_client = self.storage_client
        bucket_name = self.bucket_name

        source_bucket = storage_client.bucket(bucket_name)
        source_blob = source_bucket.blob(target_blob_name)

        # 동일 버켓내에서 복사가 이루어지는 경우
        if bucket_name == destination_bucket_name:
            destination_bucket = source_bucket
        else:
            destination_bucket = storage_client.bucket(destination_bucket_name)

        copied_blob = source_bucket.copy_blob(source_blob, destination_bucket, destination_blob_name)

        print(f"Blob {source_blob.name} in bucket {source_bucket.name} copied to blob {copied_blob.name} in bucket {destination_bucket.name}.")

    """
    delete
    """
    def delete_blob(self, delete_blob_name):

        storage_client = self.storage_client
        bucket_name = self.bucket_name

        source_bucket = storage_client.bucket(bucket_name)
        source_bucket.delete_blob(delete_blob_name)

        print(f"Blob {delete_blob_name} in bucket {source_bucket.name} has been deleted")

    """
    move = copy + delete
    """
    def move_blob(self, target_blob_name, destination_bucket_name, destination_blob_name):

        blob_test.copy_blob(self, target_blob_name, destination_bucket_name, destination_blob_name)
        blob_test.delete_blob(self, target_blob_name)

        print(f"Blob {target_blob_name} in bucket {self.bucket_name} moved to blob {destination_blob_name} in bucket {destination_bucket_name}")


if __name__ == '__main__':

    BUCKET_NAME = 'hello_test_bucket_1208'
    TARGET_BUCKET_NAME = 'test_for_connect_bucket'
    storage_client = storage.Client()
    b = blob_test(storage_client, BUCKET_NAME)
    #b.rename_blob('test1.txt', 'rename_test1.txt')
    #b.copy_blob('test2.txt', BUCKET_NAME, 'copied_test2.txt')
    #b.delete_blob('test2.txt')
    #b.move_blob('test1.txt', TARGET_BUCKET_NAME, 'moved_test1.txt')
