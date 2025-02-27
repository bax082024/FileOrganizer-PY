﻿import os
import shutil

folder_path = input("Enter the folder path where files were sorted: ").strip()

log_file = os.path.join(folder_path, "log.txt")

if not os.path.exists(log_file):
    print("No log file found. Undo operation cannot be performed.")
    exit()

with open(log_file, "r") as log:
    lines = log.readlines()

for line in lines:
    new_path, old_path = line.strip().split(" -> ")
    
    if os.path.exists(new_path):  
        shutil.move(new_path, old_path)
        print(f"Restored: {new_path} → {old_path}")
    else:
        print(f"Skipped: {new_path} (File not found)")

os.remove(log_file)
print("\nUndo completed! All files have been restored.")

