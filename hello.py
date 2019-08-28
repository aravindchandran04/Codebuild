import boto3
import requests
r = requests.get('https://google.com')
p =r.status_code


print(p)
