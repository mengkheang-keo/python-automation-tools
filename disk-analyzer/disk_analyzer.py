# import
import os

# select folder
inputFolder = input("Enter path: ")
folder = inputFolder

# variables
sizeByExt = {}
counts = {}
fileData = []

# function 
def format_size(bytes):
    KB = 1024
    MB = KB ** 2
    GB = KB ** 3

    if bytes < KB:
        return f"{bytes} B"
    elif bytes < MB:
        return f"{bytes/KB:.2f} KB"
    elif bytes < GB:
        return f"{bytes/MB:.2f} MB"
    else:
        return f"{bytes/GB:.2f} GB"

# process
print("---------------FOLDER SUMMARY-----------------")
print("Locations: ",folder)
print("----------------------------------------------")
print(f"{'Extension':25} | {'Count':5} | {'Total Size':10}")
print("----------------------------------------------")
for root, dirs, files in os.walk(folder):
    for file in files:
        fullPath = os.path.join(root, file)
        name, ext = os.path.splitext(file)
        size = os.path.getsize(fullPath)
        ext = ext.lower()
        if ext == "":
            ext = "no extension"
        # count extension and size
        if ext not in counts:
            counts[ext] = 0
            sizeByExt[ext] = 0
        counts[ext] += 1
        sizeByExt[ext] += size
# print output
for ext in sorted(sizeByExt, key=sizeByExt.get, reverse=True):
    print(f"{ext:25} | {counts[ext]:5} | {format_size(sizeByExt[ext])}")
print("----------------------------------------------")
totalFiles = sum(counts.values())
totalSize = sum(sizeByExt.values())
print(f"Total Files: {totalFiles}")
print(f"Total Size: {format_size(totalSize)}")