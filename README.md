# AWS-backup-system-PYTHON
#AWS Automated Backup and Reporting System

## Overview

AWS Automated Backup and Reporting System is a Python-based cloud automation project that automatically creates backups of Amazon EBS volumes using snapshots, manages snapshot retention, generates backup reports, uploads reports to Amazon S3, and sends email notifications containing backup statistics and execution details.

This project helps organizations automate backup operations, reduce manual effort, improve disaster recovery readiness, and maintain backup visibility through reporting and notifications.

---

## Features

✅ Automatic EBS Volume Discovery

✅ Automated EBS Snapshot Creation

✅ Snapshot Retention and Cleanup

✅ Backup Report Generation

✅ Report Upload to Amazon S3

✅ Email Notifications

✅ Error Handling

✅ Modular Project Structure

---

## Architecture

EC2 / EBS Volumes
│
▼
Create Snapshots
│
▼
Delete Old Snapshots
│
▼
Generate Report
│
▼
Upload Report to S3
│
▼
Send Email Notification
│
▼
Backup Completed

---

## Technologies Used

* Python
* AWS EC2
* AWS EBS Snapshots
* Amazon S3
* Boto3
* SMTP Email Service
* IAM

---

## Project Structure

```bash
aws-backup-system/
│
├── main.py
├── ebs_backup.py
├── cleanup.py
├── report.py
├── email_sender.py
├── s3_upload.py
└── README.md
```

### File Responsibilities

#### main.py

Main entry point of the application.

Responsibilities:

* Executes the complete workflow
* Calls backup functions
* Triggers cleanup
* Generates reports
* Uploads reports to S3
* Sends email notifications

---

#### ebs_backup.py

Handles EBS snapshot creation.

Responsibilities:

* Discover EBS volumes
* Create snapshots
* Return snapshot information

---

#### cleanup.py

Handles snapshot retention.

Responsibilities:

* Find old snapshots
* Delete expired snapshots
* Reduce storage costs

---

#### report.py

Generates backup reports.

Responsibilities:

* Create backup summary
* Save report locally
* Return report filename

---

#### email_sender.py

Handles email notifications.

Responsibilities:

* Generate email content
* Attach backup statistics
* Send success notifications

---

#### s3_upload.py

Handles S3 uploads.

Responsibilities:

* Upload report files
* Store reports securely
* Return S3 object path

---

## How It Works

### Step 1

The system scans all EBS volumes in the AWS account.

### Step 2

A snapshot is created for every volume.

### Step 3

Old snapshots exceeding the retention period are automatically deleted.

### Step 4

A backup report is generated containing:

* Number of volumes scanned
* Snapshots created
* Old snapshots deleted
* Backup status

### Step 5

The report is uploaded to Amazon S3.

### Step 6

An email notification is sent to the administrator with backup details.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/titanreon17-art/aws-backup-system.git

cd aws-backup-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure AWS credentials:

```bash
aws configure
```

Provide:

* Access Key
* Secret Key
* Region

---

## Running the Project

Run:

```bash
python main.py
```

---

## Sample Output

```text
===== AWS BACKUP SYSTEM STARTED =====
Snapshots Created: 5
Old Snapshots Deleted: 2

Report saved locally: backup_report.txt
Report uploaded to S3: reports/2026-06-29-backup_report.txt
==== Email sent successfully. ====

===== BACKUP AND EMAIL SENT SUCCESSFULLY =====

Report stored in S3 at:
reports/2026-06-29-backup_report.txt

===== SYSTEM COMPLETED =====
```

---

## Business Impact

This solution helps organizations:

* Automate backup operations
* Reduce manual intervention
* Improve disaster recovery readiness
* Maintain backup history
* Reduce operational effort
* Minimize data loss risks
* Centralize backup reporting
* Improve visibility through notifications
* Optimize storage costs using automated cleanup

---

## Real-World Use Cases

* Cloud Infrastructure Backup
* Production Server Backup
* Disaster Recovery Planning
* DevOps Automation
* Infrastructure Monitoring
* Compliance and Audit Reporting

---

## Future Enhancements

* AWS Lambda Integration
* EventBridge Scheduling
* CloudWatch Monitoring
* SNS Notifications
* Multi-Region Backups
* AWS Secrets Manager Integration
* Detailed Logging
* Dashboard Reporting
* Automated Restore Testing

---

## Author

Mehboob Siddiqui

Cloud | AWS | Python 

---

## License

This project is open-source and available under the MIT License.
