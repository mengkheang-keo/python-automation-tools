import os

# select folder
folder = "T:/Python Automation/1.Table Extraction"

# list all files in the folder
files = os.listdir(folder)

# variables
counts = {}
sizeByExt = {}
largestFile = ""
largestSize = 0

print("-------------Folder Summary------------")

for file in files:

    name, ext = os.path.splitext(file)
    fullPath = os.path.join(folder, file)

    # determine type, folder, file, or hidden files
    if os.path.isdir(fullPath):
        fileType = "Folder"
        size = 0
    else:
        fileType = "File"
        size = os.path.getsize(fullPath)

    # extension handling
    if ext == "":
        ext = "no-extension"

    if ext not in counts:
        counts[ext] = 0
        sizeByExt[ext] = 0

    counts[ext] += 1
    sizeByExt[ext] += size

    if size > largestSize:
        largestSize = size
        largestFile = file

    print(f"{fileType:7}: {name}, Extension: {ext}, Size: {(size/1024):.2f}kb")

print("--------------------------------------")

extName = ""
commonExt = 0

for ext, count in counts.items():
    if count > commonExt:
        extName = ext
        commonExt = count

    print(f"{ext:12} : {count}")

print("--------------------------------------")

totalItem = len(files)
totalUniqueExt = len(counts)

print("Total Files:", totalItem)
print("Total Unique Extension:", totalUniqueExt)
print("Most Common Extension:", extName)
print("--------------------------------------")
print(f"Largest File: {largestFile}")
print(f"Largest Size: {largestSize/1024:.2f} KB")