import boto3
ec2_client = boto3.client('ec2',region_name='us-east-1')
response = ec2_client.describe_instances()
print(response)

print("hello World")
