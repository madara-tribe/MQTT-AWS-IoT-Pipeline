import boto3
from common import TABLE_NAME
dynamodb = boto3.resource('dynamodb')

def main():
    table = dynamodb.Table(TABLE_NAME)
    response = table.scan()
    items = response['Items']
    print(items)

if __name__=="__main__":
    main()
