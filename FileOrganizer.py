import os

folder_path = input("Enter the folder path to organize: ").strip()

if not os.path.exists(folder_path):
    print("Error: The specified folder does not exist. Please check the path and try again.")
    exit()

files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]


