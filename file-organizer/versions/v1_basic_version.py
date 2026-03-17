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

# folder = input("Enter your folder path: ")
path = "T:"

# def get category
def get_category(ext):
    for category, extensions in categories.items():
        if ext in extensions:
            return category
    return "others"

# def create folder
def create_folder(category):
    category_folder = os.path.join(path, category.capitalize())
    # make directory
    os.makedirs(category_folder, exist_ok=True)
    return category_folder

# process
for file in os.listdir(path):
    full_path = os.path.join(path, file)
    if os.path.isfile(full_path):
        name, ext = os.path.splitext(file)
        ext = ext.lower()
        if ext == "":
            ext = "no extension"

        category = get_category(ext)
        category_folder = create_folder(category)
        destination = os.path.join(category_folder, file) # move file

        print(file, category)
        print(file, "→", category_folder)
        shutil.move(full_path, destination)