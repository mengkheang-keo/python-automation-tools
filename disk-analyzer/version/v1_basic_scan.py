import os

# select foler
folder = "T:/Python Automation/1.Table Extraction"

# list all files in the folder
files = os.listdir(folder)

# loop for files
counts = {}
print("------------------------")
for file in files:
    name, ext = os.path.splitext(file)
    fullPath = os.path.join(folder, file)
    size = os.path.getsize(fullPath)
    if ext == "":
        ext = "no-extension"
    if ext not in counts:
        counts[ext] = 0
    counts[ext] += 1
    print(f"file: {name} ; extension: {ext} ; path: {fullPath}; size: {(size/1024):.2f}kb")
print("------------------------")

numExt = ""
extCount = 0
for ext, count in counts.items():
    if count > extCount:
        extCount = count
        numExt = ext
    print(f"{ext:15} : {count}")
print("------------------------")

avgFileCount = sum(counts.values()) / len(counts)
totalFile = len(files)
totalUniqueExt = len(counts)
largeGroupPercent = (extCount / totalFile) * 100
print(f"total files: {totalFile} \ntotal extensions: {totalUniqueExt} \nlargest Ext: {numExt} with {extCount} \naverage file: {avgFileCount:.2f} \nLargest Extension Share: {largeGroupPercent}")