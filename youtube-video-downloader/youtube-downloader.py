import os
import yt_dlp

# use download folder as containing folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_FOLDER = os.path.join(BASE_DIR, "download")

VALID_RESOLUTIONS = ["360", "480", "720", "1080", "1440"]

# check if the video is playlist or a single video
def is_playlist(url):
    return ("list=" in url and "watch" in url) or "playlist?" in url


def download_youtube_video(url, resolution="1080", filename=None):
    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

    format_selector = (
        f"bv*[height<={resolution}][ext=mp4]+ba[ext=m4a]"
        f"/b[height<={resolution}][ext=mp4]/best"
    )

    ydl_opts = {
        "format": format_selector,
        "merge_output_format": "mp4",
        "outtmpl": "",
        "noplaylist": True,
        "quiet": False,
        "postprocessors": [
            {
                "key": "FFmpegVideoConvertor",
                "preferedformat": "mp4",
            }
        ],
    }

    # playlist download
    if is_playlist(url):
        ydl_opts["noplaylist"] = False
        ydl_opts["outtmpl"] = os.path.join(
            DOWNLOAD_FOLDER,
            "%(playlist_title)s/%(playlist_index)03d - %(title)s.%(ext)s",
        )

    # single video download
    else:
        if filename:
            if not filename.lower().endswith(".mp4"):
                filename += ".mp4"
        else:
            filename = "%(title)s.%(ext)s"

        ydl_opts["outtmpl"] = os.path.join(DOWNLOAD_FOLDER, filename)

    try:
        print("\nStarting download...")
        print(f"URL: {url}")
        print(f"Max resolution: {resolution}p")
        print(f"Saving to: {DOWNLOAD_FOLDER}\n")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("\nDownload completed!")

    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":

    url = input("Enter YouTube video or playlist URL: ").strip()

    resolution = input(
        "Enter max resolution (360, 480, 720, 1080, 1440) [default: 1080]: "
    ).strip()

    if not resolution:
        resolution = "1080"

    if resolution not in VALID_RESOLUTIONS:
        print("Invalid resolution, using default 1080p")
        resolution = "1080"

    filename = None

    # save single video with name
    if not is_playlist(url):
        filename = input(
            f"Enter filename (saved to {DOWNLOAD_FOLDER}) [leave empty for default]: "
        ).strip()

        if filename == "":
            filename = None

    download_youtube_video(url, resolution, filename)