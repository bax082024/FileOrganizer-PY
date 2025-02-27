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
    "Scripts": [".py", ".sh", ".bat", ".json"],
    "Others": []
}

files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

print("\nFound Files:")
if not files:
    print("No files found in the folder.")
    exit()

for file in files:
    print(f"- {file}")

print(f"\nStep 1 Complete: Found {len(files)} file(s) in '{folder_path}'.")

user_choice = input("\nDo you want to continue sorting these files? (yes/no): ").strip().lower()

if user_choice != "yes":
    print("Sorting canceled. No changes were made.")
    exit()

log_file = os.path.join(folder_path, "log.txt")

with open(log_file, "w") as log:
    sorted_count = 0

    for file in files:
        file_ext = os.path.splitext(file)[1].lower()
        
        category = "Others"
        for cat, extensions in file_categories.items():
            if file_ext in extensions:
                category = cat
                break

        category_folder = os.path.join(folder_path, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(category_folder, file)
        shutil.move(old_path, new_path)

        log.write(f"{new_path} -> {old_path}\n")

        print(f"Moved: {file} → {category}/")
        sorted_count += 1

print(f"\nAll {sorted_count} file(s) have been organized successfully! Log saved to 'log.txt'.")
