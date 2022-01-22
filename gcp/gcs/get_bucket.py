from google.cloud import storage

storage_client = storage.Client()

BUCKET_NAME = 'hello_test_bucket_1208'
bucket = storage_client.get_bucket(BUCKET_NAME)

bucket_metadata = \
f"""
ID : {bucket.id}
Name: {bucket.name}
Storage Class: {bucket.storage_class}
Location: {bucket.location}
Location Type: {bucket.location_type}
Cors: {bucket.cors}
Default Event Based Hold: {bucket.default_event_based_hold}
Default KMS Key Name: {bucket.default_kms_key_name}
Metageneration: {bucket.metageneration}
Public Access Prevention: {bucket.iam_configuration.public_access_prevention}
Retention Effective Time: {bucket.retention_policy_effective_time}
Retention Period: {bucket.retention_period}
Retention Policy Locked: {bucket.retention_policy_locked}
Requester Pays: {bucket.requester_pays}
Self Link: {bucket.self_link}
Time Created: {bucket.time_created}
Versioning Enabled: {bucket.versioning_enabled}
Labels: {bucket.labels}
"""

print(bucket_metadata)
