import boto3
import requests
ec2_client = boto3.client('ec2',aws_access_key_id=AKIAUMZO4WIRA5CVL6UU,aws_secret_access_key=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)


response = ec2_client.describe_instances()
print(response)

print("hello World")
