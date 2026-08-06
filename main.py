from yt_dlp import YoutubeDL
from colorama import Fore, init

init(autoreset=True)

print(Fore.BLUE + 'Universal CLI downloader')
print('You can download video from youtube, TikTok, Instagram, Pinterest and Reddit')
print("Type 'stop' to exit")
while True:
  try:
    url = input('Enter link: ')
    if url == 'stop':
      break
    else:
      ydl_opts = {}
      with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

      print(Fore.GREEN + 'Downloading finish')
  except Exception as e:
    print(Fore.RED + f'Error {e}!')