import boto3

# --- CONFIG ---
INSTANCE_ID = "i-xxxxxxxxxxxxxxxxx"  # your EC2 instance ID
EMAIL = "your_email@example.com"      # email to receive alerts
THRESHOLD = 70                        # CPU threshold %
TOPIC_NAME = "EC2-CPU-Alerts"
ALARM_NAME = "HighCPUAlarm"

# --- Clients ---
sns_client = boto3.client('sns')
cloudwatch_client = boto3.client('cloudwatch')

# 1️⃣ Create SNS topic
topic = sns_client.create_topic(Name=TOPIC_NAME)
topic_arn = topic['TopicArn']
print(f"SNS Topic created: {topic_arn}")

# 2️⃣ Subscribe email to SNS topic
sns_client.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint=EMAIL
)
print(f"Email subscription sent to {EMAIL}. Please confirm from your inbox.")

# 3️⃣ Create CloudWatch alarm
cloudwatch_client.put_metric_alarm(
    AlarmName=ALARM_NAME,
    AlarmDescription='Alarm when CPU exceeds threshold',
    ActionsEnabled=True,
    AlarmActions=[topic_arn],
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Statistic='Average',
    Dimensions=[{'Name': 'InstanceId', 'Value': INSTANCE_ID}],
    Period=60,
    EvaluationPeriods=1,
    Threshold=THRESHOLD,
    ComparisonOperator='GreaterThanThreshold'
)

print(f"CloudWatch Alarm '{ALARM_NAME}' created.")
