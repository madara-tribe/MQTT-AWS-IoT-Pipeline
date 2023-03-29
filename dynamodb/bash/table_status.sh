#/bin/sh
TABLE_NAME=wx_data
aws dynamodb describe-table --table-name $TABLE_NAME | grep TableStatus
