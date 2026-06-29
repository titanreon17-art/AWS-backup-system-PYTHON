import smtplib
from email.message import EmailMessage
from datetime import datetime


SENDER_EMAIL = "titanreon17@gmail.com"
APP_PASSWORD = "nmpk fnmi xuxz rtcw"

RECEIVER_EMAIL = "siddiquimehboob173@gmail.com"


def send_email(total_volumes,
               snapshots_created,
               deleted_snapshots):

    message = EmailMessage()

    message["Subject"] = "AWS Backup Report - SUCCESS"

    message["From"] = SENDER_EMAIL

    message["To"] = RECEIVER_EMAIL

    body = f"""
AWS Automated Backup Report

Date : {datetime.now()}

Total Volumes Scanned : {total_volumes}

Snapshots Created : {snapshots_created}

Old Snapshots Deleted : {deleted_snapshots}

Backup Status : SUCCESS

Regards,
Cloud Backup System
"""

    message.set_content(body)

    try:

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

            smtp.login(SENDER_EMAIL, APP_PASSWORD)

            smtp.send_message(message)

        print("\n==== Email sent successfully. ====")

    except Exception as e:

        print("==== Email failed:", e,"====")