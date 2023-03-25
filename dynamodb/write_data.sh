TABLE_NAME=wx_data
PRIMARY="sample_time"
SORTED="device_id"
aws dynamodb put-item \
    --table-name $TABLE_NAME  \
    --item '{$PRIMARY: {"N": "128"}, $SORTED: {"N": "888"}, "temperature": {"N": "28"}, "humidity": {"N": "80"}}'
