import boto3
from common import TABLE_NAME

def delete_dax_table(table_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    table.delete()

    print(f"Deleting {table.name}...")
    table.wait_until_not_exists()


if __name__ == '__main__':
    table_name=TABLE_NAME
    delete_dax_table(table_name)
    print("Table deleted!")
