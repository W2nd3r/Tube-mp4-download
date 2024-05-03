from pytube import YouTube
import os

# get link
url = input("Enter Link:")
yt = YouTube(url)

# getting download directory
download_path = os.path.expanduser('~/Downloads')

# for detailed description of available downloads
#print(yt.streams.filter(file_extension="mp4"))

# downloading video and where to save
stream = yt.streams.get_by_itag(22)
stream.download(download_path)
