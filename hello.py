import boto3
s3_resource = boto3.resource('s3')
response = s3_resource.list_buckets()
print(response)

print("hello World")
