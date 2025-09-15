import boto3
import json

# ---------------- CONFIG ----------------
USER_NAME = "test-user"  # Name of IAM user (can be existing)
POLICY_NAME = "ReadOnlyMyBucket"
BUCKET_NAME = "my-bucket"  # Replace with your S3 bucket name
REGION = "ap-south-1"
# ----------------------------------------

# 1️⃣ Create IAM client
iam = boto3.client("iam", region_name=REGION)

# 2️⃣ Define the policy
policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                f"arn:aws:s3:::{BUCKET_NAME}",
                f"arn:aws:s3:::{BUCKET_NAME}/*"
            ]
        }
    ]
}

# 3️⃣ Create policy
try:
    response = iam.create_policy(
        PolicyName=POLICY_NAME,
        PolicyDocument=json.dumps(policy_document)
    )
    policy_arn = response["Policy"]["Arn"]
    print(f"✅ IAM Policy created: {policy_arn}")
except iam.exceptions.EntityAlreadyExistsException:
    # Replace YOUR_ACCOUNT_ID with your AWS account ID
    policy_arn = f"arn:aws:iam::YOUR_ACCOUNT_ID:policy/{POLICY_NAME}"
    print(f"⚠️ Policy already exists. Using existing ARN: {policy_arn}")

# 4️⃣ Create IAM user (if doesn't exist)
try:
    iam.create_user(UserName=USER_NAME)
    print(f"✅ IAM User created: {USER_NAME}")
except iam.exceptions.EntityAlreadyExistsException:
    print(f"⚠️ User already exists: {USER_NAME}")

# 5️⃣ Attach policy to user
iam.attach_user_policy(
    UserName=USER_NAME,
    PolicyArn=policy_arn
)
print(f"✅ Policy '{POLICY_NAME}' attached to user '{USER_NAME}'")

# 6️⃣ Verify
attached_policies = iam.list_attached_user_policies(UserName=USER_NAME)["AttachedPolicies"]
print("📄 Attached Policies:")
for p in attached_policies:
    print(f"- {p['PolicyName']}")
