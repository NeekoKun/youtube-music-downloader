import os
from youtubesearchpython import VideosSearch

def download_audio(link):
    os.system("yt-dlp --extract-audio " + link)

def title_to_url(title):
    results = VideosSearch(title, limit=10).result()

    for i, result in enumerate(results['result']):
        print(str(i+1)+". "+result['title'])
        
    return results['result'][int(input("Input song index:\n"))-1]['link']

try:
    download_audio(title_to_url(input("Input the song title:\n")))
except KeyboardInterrupt:
    print("Youtube Music Downloader terminated")
