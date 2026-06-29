from email_sender import send_email
from ebs_backup import get_all_volumes, create_snapshot
from cleanup import delete_old_snapshots
from report import generate_report
from s3_upload import upload_report


def main():

    print("\n===== AWS BACKUP SYSTEM STARTED =====")

    volumes = get_all_volumes()

    snapshot_count = 0

    for v in volumes:
        snap = create_snapshot(v)
        if snap:
            snapshot_count += 1

    deleted = delete_old_snapshots(retention_days=7)

    print("\nSnapshots Created:", snapshot_count)
    print("Old Snapshots Deleted:", deleted)

    report_file = generate_report(snapshot_count, deleted)

    s3_path = upload_report(report_file)

    send_email(
        total_volumes=len(volumes),
        snapshots_created=snapshot_count,
        deleted_snapshots=deleted
    )

    print("\n===== BACKUP AND EMAIL SENT SUCCESSFULLY =====\n")

    print("Report stored in S3 at:", s3_path)

    print("\n===== SYSTEM COMPLETED =====\n")


if __name__ == "__main__":
    main()