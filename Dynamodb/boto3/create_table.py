import boto3
from common import TABLE_NAME, PARTITION_KEY, SOTE_KEY

def create_dax_table():
    dynamodb = boto3.resource('dynamodb')
    params = {
        'TableName': TABLE_NAME,
        'KeySchema': [
            {'AttributeName': PARTITION_KEY, 'KeyType': 'HASH'},
            {'AttributeName': SOTE_KEY, 'KeyType': 'RANGE'}
        ],
        'AttributeDefinitions': [
            {'AttributeName': PARTITION_KEY, 'AttributeType': 'S'},
            {'AttributeName': SOTE_KEY, 'AttributeType': 'N'}
        ],
        'ProvisionedThroughput': {
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    }
    table = dynamodb.create_table(**params)
    print(f"Creating {TABLE_NAME}...")
    table.wait_until_exists()
    return table


if __name__ == '__main__':
    dax_table = create_dax_table()
    print(f"Created table.")
