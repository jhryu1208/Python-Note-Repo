import os
import pandas as pd
from google.cloud import storage


class upload_blob:
    def __init__(self, s_client, b_name):
        self.storage_client = s_client
        self.bucket_name = b_name

    def upload_from_string(self, destination_blob_name, source_file_name, c_type):
        storage_client = self.storage_client
        bucket_name = self.bucket_name

        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_string(source_file_name, content_type = c_type)

        print(f'File {blob.name} uploaded to {bucket.name}')

    def upload_from_filename(self, destination_blob_name, source_file_path, c_type):
        storage_client = self.storage_client
        bucket_name = self.bucket_name

        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        # 업로드하고 싶은 파일의 디렉토리 작성
        blob.upload_from_filename(source_file_path)

        print(f'File {blob.name} uploaded to {bucket.name}')

    def upload_from_file(self, destination_blob_name, source_file_path, c_type):
        storage_client = self.storage_client
        bucket_name = self.bucket_name

        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        # 업로드하고 싶은 파일의 handler생성후 기입
        with open(source_file_path, 'rb') as f:
            blob.upload_from_fil(f, content_type = c_type)

        print(f'File {blob.name} uploaded to {bucket.name}')



if __name__ == '__main__':

    """
    create example dataframe
    """
    data = [
    ['Pierre-Emile Höjbjerg', 26, 185, 'Kopenhagen', 'Central Midfield'],
    ['Tanguy Ndombélé', 25, 181, 'Longjumeau', 'Central Midfield'],
    ['Cristian Romero', 23, 185, 'Córdoba', 'Centre-Back'],
    ['Heung-min Son', 28, 184, 'Korea, South', 'Left Winger'],
    ['Davinson Sánchez', 25, 187, 'Colombia', 'Centre-Back']
    ]
    col_list = ['name', 'age', 'height', 'place_of_bith', 'main_position']

    tottenham_csv = pd.DataFrame(data, columns = col_list).to_csv(encoding='utf-8')

    """
    main_code
    """
    TARGET_BUCKET_NAME = 'hello_test_bucket_1208'
    storage_client = storage.Client()

    b = upload_blob(storage_client, TARGET_BUCKET_NAME)
    b.upload_from_string('tottenham.csv', tottenham_csv, 'text/csv')
    b.upload_from_filename("test_upload_from_filename.txt", os.getcwd()+'/gcp/test_file/test1.txt', 'text')
    b.upload_from_filename("test_upload_from_file.txt", os.getcwd()+'/gcp/test_file/test1.txt', 'text')
