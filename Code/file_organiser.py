"""
Organizing Files by Type
✅ Objective:
This script organizes files in a folder by moving them into subfolders based on their file type (e.g., .jpg goes into Images, .pdf into Documents).

✅ Features:
✔ Detects file extensions
✔ Creates folders automatically if they don't exist
✔ Moves files into their respective folders

✅ Example:
If the folder contains the following files:
- file1.jpg
- file2.pdf
- file3.txt
- file4.jpg

The script will create the following folders and move the files:
- Images
    - file1.jpg 
    - file4.jpg
- Documents
    - file2.pdf
- Others
    - file3.txt

✅ To run the script:
- python file_organiser.py <folder_path>
  comand  line_arg1         line_arg2        line_arg3  line_arg4
- python file_organiser.py   /path/to/folder arg2       arg3
   indexes:       0               1               2       3
"""

import os
import sys
import shutil

# Step 1: Define the file-type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xls", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".webm"],
    "Music": [".mp3", ".wav", ".flac"],
    "Code": [".py", ".java", ".c", ".cpp", ".html", ".css", ".js"],
    "Others": [".*", ".**", ".***", ".***", ".", ""] # Default category for other file types
}

# Step 2: Create folders for each file type category
def create_folders(file_types):
    for folder in file_types.keys():
        if os.path.exists(folder):
            print(f"{folder} folder already exists.")
            continue
        os.mkdir(folder)

# Step 3: Move files into their respective folders from folder path

def move_files(folder_path, file_types):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name) # Get the full path of the file

        # Separate files from folders
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file_name)[1].lower() # Get the file extension file1.jpeg = ['file1','.jpeg']

            # Move the file to the respective folder
            for category, extensions in file_types.items():
                if file_extension in extensions:
                    dest_folder_path = os.path.join(folder_path, category) # created the full file path for each file category
                    if not os.path.exists(dest_folder_path):
                        os.mkdir(dest_folder_path)
                        shutil.move(file_path, dest_folder_path)
                    

                    print(f"Moved: {file_name} to {category} folder.")
                    break

# Final Step: Get the folder path from the command line arguments
if len(sys.argv) < 2:
    print("Usage: python file_organiser.py <folder_path>")
    sys.exit(1)

folder_path = sys.argv[1]

create_folders(file_types)
move_files(folder_path, file_types)
print("Files have been organized successfully.")
