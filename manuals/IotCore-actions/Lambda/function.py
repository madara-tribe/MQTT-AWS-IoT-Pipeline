import json
import time
import boto3

def lambda_handler(event, context):
    print(event["sample_time"])  
    print(event["humidity"])  
    print(event["barometer"])  
    time.sleep(1)
    
    return "OK"
