# /bin/sh
TABLE_NAME=wx_data
aws dynamodb get-item --consistent-read \
    --table-name $TABLE_NAME \
    --key '{ "sample_time": {"N": "2"}, "device_id": {"N": "3"}}'
