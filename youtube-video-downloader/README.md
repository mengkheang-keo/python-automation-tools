# YouTube Downloader

A simple Python tool for downloading YouTube videos or playlists using **yt-dlp**.

## Features
- Download single videos
- Download playlists
- Choose maximum resolution
- Automatic video/audio merging (MP4)

## Requirements
Install dependency:

pip install yt-dlp

You also need **FFmpeg** installed:
https://ffmpeg.org/download.html

Example Windows setup:
- Extract FFmpeg to `C:\ffmpeg`
- Add `C:\ffmpeg\bin` to system PATH

## Usage

Run the script:

python youtube_downloader.py

The program will prompt for:
- YouTube video or playlist URL
- Maximum resolution
- Optional filename

Sample: https://youtu.be/dQw4w9WgXcQ?si=3NrBJAldbLLtnqbj

Downloads are saved to:

download/