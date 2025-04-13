"""
Description: This Python script uses the pytube library to download a YouTube video in its highest available resolution. 
It prompts the user to enter a valid YouTube URL, displays the video's title, view count, and available streams, 
then proceeds to download the selected video while showing real-time download progress as a percentage.

Author: Olayemi Jean Clausius Odjetunde
Version: 1.0
"""



from pytube import YouTube

# use the following url to run this code = "https://www.youtube.com/watch?v=U_bjZLGm8uI"

url = input("Enter the YouTube video URL to download: ")

while "https://www.youtube.com/" not in url:
    print("ERROR")
    url = input("Enter the YouTube video URL to download: ")

def on_download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded * 100 / stream.filesize

    print(f"Download progress: {int(percent)}%")

youtube_video = YouTube(url)

youtube_video.register_on_progress_callback(on_download_progress)

print("TITLE: " + youtube_video.title)
print("VIEWS:", youtube_video.views)

print("STREAMS")
for stream in youtube_video.streams.fmt_streams:
    print("  ", stream)

stream = youtube_video.streams.get_highest_resolution()
print("Video stream: ", stream)
print("Downloading...")
stream.download()
print("DONE")

