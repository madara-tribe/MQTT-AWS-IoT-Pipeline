#/bin/bash
aws dynamodb put-item \
    --table-name wx_data  \
    --item \
        '{"sample_time": {"N": "128"}, "device_id": {"N": "888"}, "temperature": {"N": "28"}, "humidity": {"N": "80"}}'
