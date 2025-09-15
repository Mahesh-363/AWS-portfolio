import requests
import json
import boto3
from datetime import datetime

# Helper function to convert non-serializable objects
def json_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

# Initialize EC2 client
ec2_client = boto3.client('ec2', region_name='ap-south-1')

# Fetch all EC2 instances
instances = ec2_client.describe_instances()

print("EC2 Instances Info:")
print(json.dumps(instances, indent=4, default=json_serializer))

# Example: Test a public API (like JSONPlaceholder)
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

if response.status_code == 200:
    print("\nPublic API Test Successful:")
    print(json.dumps(response.json(), indent=4))
else:
    print("Public API Test Failed with status code:", response.status_code)

