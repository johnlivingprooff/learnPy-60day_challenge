import os
import sys
import shutil

# Define file-type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xls", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".webm"],
    "Music": [".mp3", ".wav", ".flac"],
    "Code": [".py", ".java", ".c", ".cpp", ".html", ".css", ".js"],
}

# Function to create a folder if it does not exist
def ensure_folder_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Move files to their respective folders
def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        sys.exit(1)
    
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file_name)[1].lower()
            destination_folder = "Others"  # Default folder
            
            for category, extensions in FILE_TYPES.items():
                if file_extension in extensions:
                    destination_folder = category
                    break
            
            dest_folder_path = os.path.join(folder_path, destination_folder)
            ensure_folder_exists(dest_folder_path)
            shutil.move(file_path, os.path.join(dest_folder_path, file_name))
            print(f"Moved: {file_name} -> {destination_folder}/")

# Main execution block
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python file_organizer.py <folder_path>")
        sys.exit(1)
    
    target_folder = sys.argv[1]
    organize_files(target_folder)
    print("Files have been organized successfully.")
