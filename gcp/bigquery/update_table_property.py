from google.cloud import bigquery

# construct a bigquery client object
client = bigquery.Client()
project_id = 'jihyun-gcp01'
dataset_id = 'test_project1'

"""
[ update_table ]
Use fields to specify which fields to update.
- param
    - table
    - fields(Sequence)

[ 테이블 프로퍼티 참조 목록 ]

partition_expiration_days(FLOAT64) : 파티션을 나눈 테이블의 모든 파티션 기본 수명(일)
expiration_timestamp(FLOAT64) : 이 테이블이 만료되는 시간
kms_key_name(STRING) : 테이블을 암호화하는 데 사용된 Cloud KMS 키의 이름
friendly_name(STRING) : 테이블을 설명하는 이름
description(STRING) : 테이블 설명
labels(ARRAY<STRUCT<STRING, STRING>>) : 테이블의 라벨을 나타내는 STRUCT 배열
require_partition_filter(BOOL) : 테이블에 대한 쿼리에 파티션 필터가 필요한지 여부
enable_refresh(BOOL) : 구체화된 뷰에 자동 새로고침이 사용 설정되었는지 여부
refresh_interval_minutes(FLOAT64) : 구체화된 뷰가 새로고침되는 빈도
"""
# description 속성을 지정하지 않았기 때문에 None이 출력된다.
table = bigquery.Table(f'{project_id}.{dataset_id}.create_table_220202')
table = client.create_table(table, exists_ok = True)
print(f'original : {table.description}') # original : None

# update_table메소드를 통해서 업데이트된 속성을 수정하지 않았기 때문에
# 다시 동일한 테이블을 불러왔을 때의 description이
# 업데이트되지 않음을 확인할 수 있다.
table = client.get_table(f'{project_id}.{dataset_id}.create_table_220202')
table.description = 'Hello I am Table!!'
table1 = client.get_table(f'{project_id}.{dataset_id}.create_table_220202')
print(f'after update : {table1.description}') # after update : None

# 반면, update_table메소드를 통해서
# 업데이트된 table의 property를 전달해주어 원본 테이블의 description속성이 수정됨을 알 수 있다.
table = client.get_table(f'{project_id}.{dataset_id}.create_table_220202')
table.description = 'Hello I am Table!!'
table = client.update_table(table,["description"]) # 업데이트 진행
table2 = client.get_table(f'{project_id}.{dataset_id}.create_table_220202')
print(f'after update : {table2.description}') # after update : Hello I am Table!!
