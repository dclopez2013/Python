

import pytube

print("*" * 60, "Welcome to the YouTube video downloader"+"*"*60)

url = input("Enter the youTube video link you wish to download\n")

youtube = pytube.YouTube(url)

#print(youtube.streams.filter(only_audio=True).all())

#print(youtube.streams.filter(only_audio=True).first())

song = youtube.streams.filter(only_audio=True).first()

song.download()