import boto3
from datetime import datetime, timezone, timedelta

ec2 = boto3.client('ec2')

def delete_old_snapshots(retention_days=7):

    try:
        snapshots = ec2.describe_snapshots(OwnerIds=['self'])

        cutoff = datetime.now(timezone.utc) - timedelta(days=retention_days)

        deleted = 0

        for snap in snapshots['Snapshots']:
            start_time = snap['StartTime']

            if start_time < cutoff:
                ec2.delete_snapshot(SnapshotId=snap['SnapshotId'])
                print(f"Deleted snapshot: {snap['SnapshotId']}")
                deleted += 1

        return deleted

    except Exception as e:
        print("Cleanup error:", e)