import boto3
from datetime import datetime

s3 = boto3.client('s3')

BUCKET_NAME = "mehboob-123-755216754844-ap-south-1-an"


def upload_report(file_name):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        s3_key = f"reports/{timestamp}-{file_name}"

        s3.upload_file(file_name, BUCKET_NAME, s3_key)

        print(f"Report uploaded to S3: {s3_key}\n")

        return s3_key

    except Exception as e:
        print("S3 upload failed:", e)
        return None