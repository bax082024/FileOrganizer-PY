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
    "Scripts": [".py", ".sh", ".bat", "json"],
    "Others": []
}

files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

print("\n Found Files:")
for file in files:
    print(f"- {file}")


print("\n Step 1 Complete: Folder scanned successfully!")

# Organizing files
for file in files:
    file_ext = os.path.splitext(file)[1].lower()  # Get file extension
    
    # Find the category for the file extension
    category = "Others"
    for cat, extensions in file_categories.items():
        if file_ext in extensions:
            category = cat
            break

    # Create category folder if it doesn't exist
    category_folder = os.path.join(folder_path, category)
    if not os.path.exists(category_folder):
        os.makedirs(category_folder)

    # Move file to the appropriate folder
    old_path = os.path.join(folder_path, file)
    new_path = os.path.join(category_folder, file)
    shutil.move(old_path, new_path)

    print(f"Moved: {file} → {category}/")

print("\nAll files have been organized successfully!")
