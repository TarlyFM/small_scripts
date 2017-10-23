"""
Song manager

Ensure downloading, cleaning and storing songs.
"""
import youtube_dl
import os
import sys
import subprocess

_DESTINATION = os.environ['HOME'] + "/Music/"

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'error':
        pass

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'logger': MyLogger(),
    'outtmpl': '/tmp/youtube_dl/%(title)s-%(id)s.%(ext)s',
    'progress_hooks': [my_hook],
    'noplaylist': True,
}

def downloader(link, callback=None, **args):
    """
    Where the magic happens
    """
    if not os.path.exists(_DESTINATION):
        os.makedirs(_DESTINATION)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    for file in os.listdir('/tmp/youtube_dl/'):
        output = '"' + _DESTINATION + file + '"'
        ffmpeg = 'ffmpeg -i "/tmp/youtube_dl/' + file + '" -af silenceremove=1:0:-50dB ' + output
        os.system(ffmpeg)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        downloader(sys.argv[1])
