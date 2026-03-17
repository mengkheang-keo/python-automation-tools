# imports
import os
import shutil
from datetime import datetime

# dictionary
categories = {
    "photos": [".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp"],
    "videos": [".mp4", ".mkv", ".avi", ".mov"],
    "documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "code": [".py", ".js", ".html", ".css", ".cpp", ".java", ".json"],
    "compressed": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "music": [".mp3", ".wav", ".flac"],
    "programs": [".exe"]
}

# directory path
path = input("Enter your folder path: ")

# def return category
def get_category(ext):
    for category, extensions in categories.items():
        if ext in extensions:
            return category
    return "others"
    
# def create folders
def create_folder(category):
    category_folder = os.path.join(path, category.capitalize())
    # create directory
    os.makedirs(category_folder, exist_ok=True)
    return category_folder

# process #1 - preview
preview = {}

for file in os.listdir(path):
    full_path = os.path.join(path, file)

    if os.path.isfile(full_path):
        name, ext = os.path.splitext(file)
        ext = ext.lower()

        if ext == "":
            ext = "no extension"

        category = get_category(ext)
        if category not in preview:
            preview[category] = []
        preview[category].append(file)
if not preview:
    print("No files to organize. Folder is clean ✨")
    exit()

# print with category as base
print("--------------------File Organizer--------------------")
for category, files in preview.items():
    print(f"{category.capitalize()}:")
    for file in files:
        print(f"       {file}")

# process #2 - confirm move
print("------------------------------------------------------")
confirmMove = input("Move these files? (Y/N): ").upper()

# process #3 - move files
if confirmMove == "Y":
    for file in os.listdir(path):
        full_path = os.path.join(path, file)

        if os.path.isfile(full_path):
            name, ext = os.path.splitext(file)

            if ext == "":
                ext = "no extension"
            category = get_category(ext)
            category_folder = create_folder(category)
            destination = os.path.join(category_folder, file)

            # prevent recursive
            if full_path != destination:
                shutil.move(full_path, destination)
                print(f"Moved {file} → {category.capitalize()}")
            else:
                print(f"Skipped {file} (already in correct folder)")
else:
    print("Operation cancelled!")












# isMoveTrue = input("Would you like to moves files (Y/N):")
# if isMoveTrue == "Y":       
#     # move file to destination folder
#     destination = os.path.join(category_folder, file)
# else:
#     print("Operation cancelled")

#         print(file, category)
#         print(file, "→", category_folder)
#         shutil.move(full_path, destination)