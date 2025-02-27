import os
import shutil

folder_path = input("Enter the folder path where files were sorted: ").strip()

log_file = os.path.join(folder_path, "log.txt")

if not os.path.exists(log_file):
    print("No log file found. Undo operation cannot be performed.")
    exit()

with open(log_file, "r") as log:
    lines = log.readlines()

restored_count = 0
skipped_count = 0

for line in lines:
    new_path, old_path = line.strip().split(" -> ")

    original_folder = os.path.dirname(old_path)
    if not os.path.exists(original_folder):
        os.makedirs(original_folder)

    if os.path.exists(new_path):
        shutil.move(new_path, old_path)
        print(f"Restored: {new_path} → {old_path}")
        restored_count += 1
    else:
        print(f"Skipped: {new_path} (File not found)")
        skipped_count += 1

os.remove(log_file)

print(f"\nUndo completed! {restored_count} file(s) restored, {skipped_count} skipped.")
