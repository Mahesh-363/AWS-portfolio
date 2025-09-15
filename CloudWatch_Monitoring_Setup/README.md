# CloudWatch Monitoring Setup

This project demonstrates how to automate the creation of an **AWS CloudWatch Alarm** for EC2 instances using **Python (Boto3)**.  

## 📌 Overview
- Monitors **CPU Utilization** of an EC2 instance.
- Creates a **CloudWatch Alarm** automatically.
- Can integrate with **SNS** for email/SMS notifications when the threshold is crossed.

## 🛠 Technologies Used
- Python 3  
- AWS Boto3 SDK  
- AWS CLI  

## ⚙️ How It Works
1. You provide your **EC2 Instance ID** in the script.
2. The script calls AWS CloudWatch via Boto3 to create an alarm.
3. Alarm triggers if CPU usage exceeds **70%** over a 5-minute period.
4. (Optional) SNS integration sends alerts to your email.

## 📂 Files
- `create_cloudwatch_alarm.py` — Python script to create the CloudWatch alarm.
- `README.md` — This file.

## 🚀 How to Run
1. Configure AWS CLI with your credentials:  
   ```bash
   aws configure
