import boto3

# Create EC2 client
ec2 = boto3.client('ec2', region_name='ap-south-1')

# Snapshot the volume
response = ec2.create_snapshot(
    VolumeId='vol-034ac2405c4391403',
    Description='My snapshot from project'
)

print("Snapshot created:")
print(response)

