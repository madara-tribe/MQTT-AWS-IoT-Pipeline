certificateArn="arn:aws:iot:ap-northeast-1:980023311172:cert/9c84a3*****************************"


# check endpoint
aws iot describe-endpoint --endpoint-type IoT:Data-ATS

# create thing
aws iot create-thing --thing-name "DevCliTestThing"

# create AWSIoT policy
aws iot create-policy --policy-name "DevCliTestThingPolicy" --policy-document "file://~/policies/dev_cli_test_thing_policy.json"

# attach policy to device certification 
aws iot attach-policy --policy-name "DevCliTestThingPolicy" --target $certificateArn

# attach device certification AWS IoT thing
aws iot attach-thing-principal --thing-name "DevCliTestThing" --principal $certificateArn
