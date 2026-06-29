import boto3
from datetime import datetime

ec2 = boto3.client('ec2')


def get_all_volumes():
    """Fetch all EBS volumes"""
    response = ec2.describe_volumes()

    volumes = []

    for vol in response['Volumes']:
        volumes.append(vol['VolumeId'])

    return volumes


def create_snapshot(volume_id):
    """Create snapshot for a single volume"""
    try:
        description = f"AutoBackup-{volume_id}-{datetime.now()}"

        response = ec2.create_snapshot(
            VolumeId=volume_id,
            Description=description
        )

        snapshot_id = response['SnapshotId']
        print(f"Snapshot created for {volume_id} → {snapshot_id}")

        return snapshot_id

    except Exception as e:
        print(f"Error for {volume_id}: {e}")
        return None