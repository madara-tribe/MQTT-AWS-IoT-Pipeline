import boto3
import os
from create_bucket import add_access_permission
from common import BUCKET_NAME, REGION, ACCESS_KEY, SECRET_KEY

def bucket_empty():
    os.system("aws s3 rm s3://{} --recursive".format(BUCKET_NAME))

def delete_bucket():
    bucket_empty()
    client = add_access_permission()
    client.delete_bucket(Bucket=BUCKET_NAME)
    print("delete s3 bucket ", BUCKET_NAME)

if __name__=="__main__":
    delete_bucket()
