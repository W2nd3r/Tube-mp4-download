from pytube import YouTube
import os

# Get link
url = input("Enter Link:")
yt = YouTube(url)

# getting download directory
download_path = os.path.expanduser('~/Downloads')

# Filter streams by file extension
streams = yt.streams.filter(file_extension="mp4")

if streams:
    # Print available streams
    print("Available streams:")
    for i, stream in enumerate(streams):
        print(f"{i+1}. {stream}")

    # Choose a stream
    choice = int(input("Enter the number of the stream you want to download: "))
    selected_stream = streams[choice-1]

    # Download selected stream
    selected_stream.download(download_path)
    print("Download completed.")
else:
    print("No streams available for download.")
