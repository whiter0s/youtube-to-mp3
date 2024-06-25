import sys
from pytube import YouTube
import moviepy

if len(sys.argv) != 3:
    print(f"Usage:{sys.argv[0]} [url] [filename to save]")
    sys.exit(0)

try:
    youtube_link = YouTube(sys.argv[1])
except Exception as error:
    print("[-]Link is invalid!")

if sys.argv[2] == "high":
    quality = youtube_link.streams.get_highest_resolution()
if sys.argv[2] == "low":
    quality = youtube_link.streams.get_highest_resolution()

quality.download(filename=sys.argv[3])
    