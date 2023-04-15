TABLE_NAME=wx_data
PRIMARY=sample_time
SOTEDKEY=device_id
aws dynamodb create-table \
    --table-name $TABLE_NAME \
    --attribute-definitions \
        AttributeName=$PRIMARY,AttributeType=N \
        AttributeName=$SOTEDKEY,AttributeType=N \
    --key-schema \
        AttributeName=$PRIMARY,KeyType=HASH \
        AttributeName=$SOTEDKEY,KeyType=RANGE \
    --provisioned-throughput \
        ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --table-class STANDARD
