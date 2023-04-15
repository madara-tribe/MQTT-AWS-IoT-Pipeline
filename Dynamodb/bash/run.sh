$ ./createTable.sh
## return_result.txt 
$ aws dynamodb describe-table --table-name wx_data | grep TableStatus
#  "TableStatus": "ACTIVE",

# if table is ACTIVE, point-in-time recovery (point-in-time リカバリとは、特定の時点までのデータ変更のリカバリのことです。 一般に、この種類のリカバリは、サーバーをバックアップが行われた時点の状態にする完全バックアップのリストア後に実行されます)
$ aws dynamodb update-continuous-backups --table-name wx_data --point-in-time-recovery-specification PointInTimeRecoveryEnabled=true         
>>>
{
    "ContinuousBackupsDescription": {
        "ContinuousBackupsStatus": "ENABLED",
        "PointInTimeRecoveryDescription": {
            "PointInTimeRecoveryStatus": "ENABLED",
            "EarliestRestorableDateTime": "2023-03-23T17:37:52+09:00",
            "LatestRestorableDateTime": "2023-03-23T17:37:52+09:00"
        }
    }
}

# putin item
$ aws dynamodb put-item \
    --table-name wx_data  \
    --item \
        '{"sample_time": {"N": "128"}, "device_id": {"N": "888"}, "temperature": {"N": "28"}, "humidity": {"N": "80"}}'

# get data
$ aws dynamodb get-item --consistent-read \
    --table-name wx_data \
    --key '{ "sample_time": {"N": "128"}, "device_id": {"N": "888"}}'
>>>
{
    "Item": {
        "device_id": {
            "N": "888"
        },
        "humidity": {
            "N": "80"
        },
        "sample_time": {
            "N": "128"
        },
        "temperature": {
            "N": "28"
        }
    }
}

