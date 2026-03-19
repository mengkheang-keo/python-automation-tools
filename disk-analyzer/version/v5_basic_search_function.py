# import
import os

# select folder
path = input("Enter path: ")
if len(path) == 2 and path.endswith(":"):
    path += "\\"

# skip some unwanted windows folders
skip_folders = ["$RECYCLE.BIN", "System Volume Information"]

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
    
# def search file name
def searchFile(searchFileName):
    index = 1
    searchLimit = 20
    countFileFromSearch = 0

    print(f"{'No.':<3} {'Name':30} | {'Size':>10} | Path")
    print("-" * 103)
    for file in fileData:
        if searchFileName in file["name"].lower():
            countFileFromSearch += 1

            if index <= searchLimit:
                relative_path = os.path.relpath(file["path"], path)

                if len(relative_path) > 50:
                    relative_path = "..." + relative_path[-50:]

                name = file["name"]
                if len(name) > 30:
                    name = name[:27] + "..."
                    print(f"{index:<3} {name:30} | {format_size(file['size']):>10} | {relative_path}")
                    index += 1
    print("-" *103)
    if countFileFromSearch > searchLimit:
        print(f"Found {countFileFromSearch} files (showing first {searchLimit})")
    else:
        print(f"Found {countFileFromSearch} files")

# def scan folder
def scan(folder):
    try:
            for item in os.listdir(folder):
                fullPath = os.path.join(folder, item)

                if os.path.isfile(fullPath):
                    name, ext = os.path.splitext(item)
                    size = os.path.getsize(fullPath)
                    ext = ext.lower()

                    if ext == "":
                        ext = "no extension"

                    if ext not in counts:
                        counts[ext] = 0
                        sizeByExt[ext] = 0

                    counts[ext] += 1
                    sizeByExt[ext] += size
                    
                    # append fileData[]
                    fileData.append({
                        "name": item,
                        "path": fullPath,
                        "ext": ext,
                        "size": size
                    })
                
                elif os.path.isdir(fullPath):
                    if item in skip_folders:
                        continue
                    scan(fullPath)
    except PermissionError:
        pass


# process
print("---------------FOLDER SUMMARY-----------------")
print("Locations: ",path)
print("----------------------------------------------")
print(f"{'Extension':25} | {'Count':5} | {'Total Size':10}")
print("----------------------------------------------")

# def scan folder process
scan(path)

# print output
for ext in sorted(sizeByExt, key=sizeByExt.get, reverse=True):
    print(f"{ext:25} | {counts[ext]:5} | {format_size(sizeByExt[ext])}")

print("----------------------------------------------")
totalFiles = sum(counts.values())
totalSize = sum(sizeByExt.values())
print(f"Total Files: {totalFiles}")
print(f"Total Size: {format_size(totalSize)}")

print("----------------------------------------------")
functionChoice = input("More functions: ")
if functionChoice == "1":
    searchFileName = input("Search: ").lower()
    print("-" *103)
    searchFile(searchFileName)