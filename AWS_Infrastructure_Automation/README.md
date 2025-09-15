# AWS Infrastructure Automation – EC2 Snapshot

## Project Overview
This project automates the creation of snapshots for Amazon EC2 volumes using **Python** and **Boto3**. Snapshots are critical for backup, disaster recovery, and system maintenance.

## Features
- Automatically create snapshots of specified EC2 volumes.
- Prints snapshot details after creation.
- Works for any EC2 volume in your AWS account.

## Prerequisites
- Python 3.x installed
- `boto3` library installed (`pip install boto3`)
- AWS CLI configured with access key, secret key, and default region
- Active EC2 instance with a volume to snapshot

## Steps to Run
1. Clone or navigate to this project directory.
2. (Optional) Activate your virtual environment:
   ```bash
   source venv/bin/activate
