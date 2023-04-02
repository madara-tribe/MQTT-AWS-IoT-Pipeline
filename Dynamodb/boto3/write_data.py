import boto3
import numpy as np
from common import TABLE_NAME, PARTITION_KEY, SOTE_KEY

def item_resource():
    temperature = int(np.random.randint(1, 30, 1))
    humidity = int(np.random.randint(1, 100, 1))
    return temperature, humidity

def write_data_to_dax_table(key_count):
    dynamodb= boto3.resource('dynamodb')
    table = dynamodb.Table(TABLE_NAME)

    for partition_key in range(1, key_count + 1):
        for sort_key in range(1, key_count + 1):
            temperature, humidity = item_resource()
            table.put_item(Item={
                PARTITION_KEY : partition_key,
                SOTE_KEY : sort_key,
                'temperature': temperature,
                'humidity':humidity
            })
            print(f"Put item ({partition_key}, {sort_key}) succeeded.")


if __name__ == '__main__':
    write_key_count = 5
    print(f"Writing {write_key_count*write_key_count} items to the table. "
          f"Each item is {write_key_count} characters.")
    write_data_to_dax_table(write_key_count)
