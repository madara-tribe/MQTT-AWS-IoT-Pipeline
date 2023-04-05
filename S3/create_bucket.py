import boto3
from common import BUCKET_NAME, REGION, ACCESS_KEY, SECRET_KEY


def add_access_permission():
    client = boto3.client('s3',
                      region_name=REGION,
                      aws_access_key_id =ACCESS_KEY,
                      aws_secret_access_key =SECRET_KEY)
    return client

def put_versioning(client):
    client.put_bucket_versioning(
        Bucket=BUCKET_NAME,
        VersioningConfiguration={'Status': 'Enabled'})
    client.get_bucket_versioning(Bucket=BUCKET_NAME)

def create_bucket():
    client = add_access_permission()   
    client.create_bucket(Bucket=BUCKET_NAME,
                  CreateBucketConfiguration={'LocationConstraint': REGION})
    print("create s3 bucket {}".format(BUCKET_NAME))
    put_versioning(client)
if __name__=="__main__":
    create_bucket()
    
