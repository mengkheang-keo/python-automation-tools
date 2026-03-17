# File Organizer

A Python script that automatically organizes files into categorized folders based on their file type.

This tool helps clean up messy directories by grouping files into structured folders like **Photos**, **Documents**, **Programs**, and more.

---

## Features

* Categorizes files by extension
* Automatically creates folders (e.g., `Photos/`, `Documents/`)
* Preview mode before moving files
* Confirmation prompt (safe execution)
* Prevents overwriting existing files
* Skips already organized folders

---

## How It Works

The script follows a simple pipeline:

1. Scan files in a directory
2. Detect file extensions
3. Map extensions to categories
4. Preview the result
5. Move files into categorized folders

---

## Example

Before:

```
test-folder/
    IMG-1.png
    IMG-2.png
    README.txt
    Minecraft.exe
```

After:

```
test-folder/
    Photos/
        IMG-1.png
        IMG-2.png

    Documents/
        README.txt

    Programs/
        Minecraft.exe
```

---

## Usage

1. Open the script and set your target folder:

```python
path = "D:/your-folder"
```

2. Run the script:

```
python file-organizer.py
```

3. Review the preview

4. Confirm when prompted:

```
Move these files? (Y/N):
```

---

## Supported Categories

* Photos (`.png`, `.jpg`, `.jpeg`, `.gif`, ...)
* Videos (`.mp4`, `.mkv`, ...)
* Documents (`.pdf`, `.txt`, `.docx`, ...)
* Code (`.py`, `.js`, ...)
* Compressed (`.zip`, `.rar`, ...)
* Music (`.mp3`, `.wav`, ...)
* Programs (`.exe`)
* Others (fallback)

---

## Notes

* The script currently scans only the top-level directory (non-recursive)
* Safe to test on a sample folder before using on important data

---

## Future Improvements

* Recursive folder support
* Duplicate file detection
* Date-based organization (e.g., `Photos/2025/`)
* CLI arguments (no need to edit code)

---

## Purpose

Built as part of a Python automation learning journey.

Focus areas:

* File system automation
* Data classification
* Safe scripting practices
