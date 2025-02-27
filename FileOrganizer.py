import os
import shutil

folder_path = input("Enter the folder path to organize: ").strip()

if not os.path.exists(folder_path):
    print("Error: The specified folder does not exist. Please check the path and try again.")
    exit()

file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".csv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Executables": [".exe", ".msi"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".sh", ".bat"],
    "Others": []  # Unsorted files go here
}

files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

print("\n Found Files:")
for file in files:
    print(f"- {file}")


print("\n Step 1 Complete: Folder scanned successfully!")
