import yt_dlp
from youtubesearchpython import VideosSearch

def download_audio(link):
  with yt_dlp.YoutubeDL({'extract_audio': True, 'format': 'bestaudio', 'outtmpl': '%(title)s.mp3'}) as video:
    info_dict = video.extract_info(link, download = True)
    video_title = info_dict['title']
    print(video_title)
    video.download(link)    
    print("Successfully Downloaded - see local folder on Google Colab")

def title_to_url(title):
    result = VideosSearch(title, limit=1)

    return result.result()['result'][0]['link']

try:
    download_audio(title_to_url(input("Input the song title:\n")))
except KeyboardInterrupt:
    print("Youtube Music Downloader terminated")
