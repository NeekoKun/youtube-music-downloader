import os
from youtubesearchpython import VideosSearch

def download_audio(link, name=None):
    if name:
        os.system("yt-dlp -q -o " + name + " --extract-audio " + link)
    else:
        os.system("yt-dlp -q --extract-audio " + link)

def title_to_url(title):
    results = VideosSearch(title, limit=10).result()

    for i, result in enumerate(results['result']):
        print(str(i+1)+". "+result['title'])
        
    return results['result'][int(input("Input song index:\n"))-1]['link']

while True:
    try:
        url = title_to_url("Input song title:\n")

        name = None
        if len(nm := input("File name:\n")) > 0:
            name = nm

        download_audio(url, name)

    except KeyboardInterrupt:
        print("Youtube Music Downloader terminated")
        break
