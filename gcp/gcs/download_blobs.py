
import os
import pandas as pd
from io import StringIO
from google.cloud import storage


class download_blobs:
    def __init__(self, s_client, source_bucket):
        self.storage_client = s_client
        self.bucket = source_bucket

    def download_as_string(self, target_blob_name):
        storage_client = self.storage_client
        bucket = self.bucket

        source_bucket = storage_client.bucket(bucket)
        target_blob = source_bucket.blob(target_blob_name)

        """
        Download the contents of this blob as bytes object
        return type : bytes
        raises : google.cloud.execptions.NotFound
        """
        return target_blob.download_as_string()

    def download_as_text(self, target_blob_name):
        storage_client = self.storage_client
        bucket = self.bucket

        source_bucket = storage_client.bucket(bucket)
        target_blob = source_bucket.blob(target_blob_name)

        """
        Download the contents of this blob as text (not bytes)
        return type : text
        -> encoding parameter!!
        """
        return target_blob.download_as_text(encoding='utf-8')

    def download_to_file(self, target_blob_name, path):
        storage_client = self.storage_client
        bucket = self.bucket

        source_bucket = storage_client.bucket(bucket)
        target_blob = source_bucket.blob(target_blob_name)

        """
        Download the contents of this blob into a file-like object
        Raises : google.cloud.exceptions.NotFound
        """
        with open(path, 'wb') as f:
            target_blob.download_to_file(f)

        print('download_to_file succeed!')

    def download_to_filename(self, target_blob_name, path):
        storage_client = self.storage_client
        bucket = self.bucket

        source_bucket = storage_client.bucket(bucket)
        target_blob = source_bucket.blob(target_blob_name)

        """
        Download the contents of this blob into a named file
        Raises : google.cloud.exceptions.NotFound
        """
        target_blob.download_to_filename(path)

        print('download_to_filename succeed!')

    def from_string(self, uri):
        """
        [Parameters]
        uri: the blob uri pass to get blob object
        client: (optional) the client to use. application code shuld always pass client
        [Return Type]
        google.cloud.storage.blob.Blob
        [Return]
        The blob object created
        """
        from google.cloud.storage.blob import Blob
        blob = Blob.from_string(uri, client = self.storage_client)

        with blob.open('rt', encoding = 'utf-8') as f:
            return f.read()


if __name__ == '__main__':

    def download_to_df(input):
        if isinstance(input, bytes) == True:
            data = StringIO(str(input, 'utf-8'))
            return pd.read_csv(data)
        elif isinstance(input, str) == True:
            data = StringIO(input)
            return pd.read_csv(data, sep = ',')

    SOURCE_BUCKET_NAME = 'hello_test_bucket_1208'
    TARGET_FILE_NAME = 'tottenham.csv'
    DOWNLOAD_PATH = os.getcwd()+'/gcp/test_file/'
    GCS_FILE_URI = f'gs://{SOURCE_BUCKET_NAME}/{TARGET_FILE_NAME}'
    storage_client = storage.Client()

    b = download_blobs(storage_client, SOURCE_BUCKET_NAME)

    result0 = b.download_as_string(TARGET_FILE_NAME)
    result0_df = download_to_df(result0)
    print(type(result0))
    print(result0_df)

    return1 = b.download_as_text(TARGET_FILE_NAME)
    return1_df = download_to_df(return1)
    print(type(return1))
    print(return1_df)

    b.download_to_file(TARGET_FILE_NAME, DOWNLOAD_PATH+'download_tottenham0.csv')

    b.download_to_filename(TARGET_FILE_NAME, DOWNLOAD_PATH+'download_tottenham1.csv')

    return2 = b.from_string(GCS_FILE_URI)
    print(download_to_df(return2))
