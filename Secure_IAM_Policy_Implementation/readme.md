# Secure IAM Policy Implementation

This project demonstrates how to create a **least-privilege IAM policy** in AWS and attach it to a user using **Python (Boto3)** and **AWS CLI**.  
It ensures secure access control following best practices.

## ✅ Features
- Create a custom IAM policy with **read-only access** to a specific S3 bucket.
- Attach the policy to an IAM user.
- Fully automated using Python (Boto3) — no AWS Console needed.
- Verifies attached policies after creation.

## 🗂 Project Files
- `create_iam_policy.py` — Python script that automates policy creation and attachment.
- `read_only_s3_policy.json` — IAM policy JSON file.
- `README.md` — Project description.

## ⚙️ How to Run
1. **Navigate to project folder**:
   ```bash
   cd ~/Desktop/AWS-Portfolio/Secure_IAM_Policy_Implementation
