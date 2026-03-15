# import
import os

# select folder
folder = "T:/Python Automation/1.Table Extraction"

# list all files in the folder
files = os.listdir(folder)

sizeByExt = {}
counts = {}
print(f"{'Extension':10} | {'Count':5} | {'Total Size':10}")
print("-------------------------------")
for root, dirs, files in os.walk(folder):
    for file in files:
        fullPath = os.path.join(root, file)
        name, ext = os.path.splitext(file)
        size = os.path.getsize(fullPath)
        if ext == "":
            ext = "no extension"
            size = 0
        if ext not in counts:
            counts[ext] = 0
            sizeByExt[ext] = 0
        counts[ext] += 1
        sizeByExt[ext] += size
# print output
for ext in sorted(sizeByExt, key=sizeByExt.get, reverse=True):
    print(f"{ext:10} | {counts[ext]:5} | {(sizeByExt[ext]/1024):8.2f}kb")

print("-------------------------------")