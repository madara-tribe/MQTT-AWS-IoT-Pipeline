import json
import time
import boto3

BUCKET_NAME="iotcoremeteo"
REGION='ap-northeast-1'
ACCESS_KEY='****************'
SECRET_KEY='****************'

def add_access_permission():
    client = boto3.client('s3',
                      region_name=REGION,
                      aws_access_key_id =ACCESS_KEY,
                      aws_secret_access_key =SECRET_KEY)
    return client
    
s3 = add_access_permission()
def lambda_handler(event, context):
    file_contents = {}
    file_contents["humidity"]=int(event["humidity"])
    file_contents["barometer"]=int(event["barometer"])
    key = str(event["sample_time"])+'.json'
    response = s3.put_object(Body=json.dumps(file_contents), Bucket=BUCKET_NAME, Key=key)
    time.sleep(1)
    return response
