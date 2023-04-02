import boto3
from common import TABLE_NAME, PARTITION_KEY, SOTE_KEY
#dynamodb = boto3.resource('dynamodb')
client = boto3.client('dynamodb')
def main():
    response = client.describe_table(TableName=TABLE_NAME)
    print(response)
if __name__=="__main__":
    main()
