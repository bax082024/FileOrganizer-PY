# Bulk File Organizer

The Bulk File Organizer is a Python script that automatically sorts files into categorized subfolders based on file types. 
It helps keep directories organized by moving files into appropriate folders, supports custom categories,
and includes an undo feature to restore files to their original locations.

---

## Features

- **Automatic File Sorting** – Moves files into folders based on extensions.
- **Custom Categories** – Users can define their own sorting rules.
- **Undo Sorting** – Restore files to their original location.
- **Log File (`log.txt`)** – Records all file movements with timestamps.
- **View & Export Log** – Users can view or export the log file after sorting.
- **Error Handling** – Handles missing files, prevents crashes, and recreates deleted folders.

---

## Installation

1. Make sure you have **Python 3.x** installed.
2. clone repository or download script :
	- https://github.com/bax082024/FileOrganizer-PY.git
3. Run the script :
	- To Organize files, open terminal or cmd and run : `python FileOrganizer.py`
	- To Undo And Restore files, open terminal or cmd and run : `python UndoOrganizer.py`

---

## How it works 

1. **Choose a Folder:**

- user selects a directory (ex, Downloads).

2. **Scan & Display Files:**

- The script lists all files found.

- The user confirms if they want to proceed.

3. **Choose Sorting Method:**

- Use default categories or define custom categories.

- If using custom categories:

	- Enter a category name (ex, Photos, jpg-files etc).

	- Enter file extensions for that category (ex, .jpg, .png).

	- Repeat until all categories are added.

4. **Sorting Process:**

- The script moves files into corresponding subfolders.

- A `log.txt` file is created to track movements.

5. **View & Export Log**

- Users can view the log after sorting.

- Option to export the log to another folder.

6. **Undo Sorting (Restore Files):**

- Run **UndoOrganizer.py** to restore files.

- The script reads `log.txt` and moves files back.

---


