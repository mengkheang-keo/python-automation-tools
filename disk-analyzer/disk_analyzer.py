# import
import os
import time

# select folder
path = input("Enter path: ")

# format Path
if len(path) == 1:
    path += ":\\"
elif len(path) == 2 and path.endswith(":"):
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
    searchLimit = 20
    results = []

    print(f"{'No.':<3} {'Name':30} | {'Size':>10} | Path")
    print("-" * 103)

    # give score ranking on search
    for file in fileData:
        score = search_score(file, searchFileName)

        if score > 0:
            results.append((score, file))

    # sort by search ranking
    results.sort(key=lambda x: x[0], reverse=True)

    # prints
    for index, (score, file) in enumerate(results[:searchLimit], 1):
        relative_path = os.path.relpath(file["path"], path)

        if len(relative_path) > 50:
            relative_path = "..." + relative_path[-50:]

        name = file["name"]
        if len(name) > 30:
            name = name[:27] + "..."

        print(f"{index:<3} {name:30} | {format_size(file['size']):>10} | {relative_path}")

    print("-" *103)

    total_found = len(results)

    if total_found > searchLimit:
        print(f"Found {total_found} files (showing first {searchLimit})")
    else:
        print(f"Found {total_found} files")

# def search scoring
def search_score(file, search):
    base = file["base"]
    if search == base:
        return 100
    elif base.startswith(search):
        return 50
    elif search in base:
        return 10
    else:
        return 0

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
                    "base": name.lower(),
                    "ext": ext.lower(),
                    "path": fullPath,
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
print("Scanning... this may take a while for large drives.")

# duration for scanning process
startTime = time.time()

# def scan folder process
scan(path)

print("----------------------------------------------")
print(f"{'Extension':25} | {'Count':5} | {'Total Size':10}")
print("----------------------------------------------")

# print output
for ext in sorted(sizeByExt, key=sizeByExt.get, reverse=True):
    print(f"{ext:25} | {counts[ext]:5} | {format_size(sizeByExt[ext])}")

print("----------------------------------------------")
totalFiles = sum(counts.values())
totalSize = sum(sizeByExt.values())
print(f"Total Files: {totalFiles}")
print(f"Total Size: {format_size(totalSize)}")
print("-" * 46)
print(f"Total time taken: {(time.time() - startTime):.2f}s")
print("----------------------------------------------")

searchFileName = input("\nSearch (or press Enter to exit): ").lower()

if searchFileName:
    print("-" *103)
    searchFile(searchFileName)