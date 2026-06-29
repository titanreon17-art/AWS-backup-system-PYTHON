def generate_report(snapshot_count, deleted_count):

    file_name = "backup_report.txt"

    with open(file_name, "w") as f:
        f.write("===== AWS BACKUP REPORT =====\n\n")
        f.write(f"Snapshots Created: {snapshot_count}\n")
        f.write(f"Old Snapshots Deleted: {deleted_count}\n")

    print("Report saved locally:", file_name)

    return file_name