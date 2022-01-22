# Imports the Google Cloud client library
from google.cloud import storage

"""
(상단) 환경 변수 등록 O
(하단) 환경 변수 등록 X
"""
storage_client = storage.Client() # client 초기화
#storage_client = storage.Client.from_service_account_json('YOUR_SECRET_KEY_DIR')


bucket_name = "test_for_connect_bucket"
bucket = storage_client.create_bucket(bucket_name) # 새로운 bucket 생성
