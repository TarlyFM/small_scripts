"""
Song manager

Ensure downloading, cleaning and storing songs.
"""
import youtube_dl
import os
import sys
import subprocess

_DEFAULT_PATH = "/tmp/youtube_dl/"
_DEFAULT_OUTPUT = os.environ['HOME'] + '/Music'

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'error':
        raise DownloadError("Ma bite")

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'logger': MyLogger(),
    'outtmpl': _DEFAULT_PATH + '%(title)s-%(id)s.%(ext)s',
    'progress_hooks': [my_hook],
    'noplaylist': True,
}

def download(link, destination=_DEFAULT_PATH):
    """
    Where the magic happens
    """
    result = ""

    if not os.path.exists(destination):
        os.makedirs(destination)

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
        temp = ydl.extract_info(link)
        result = os.path.splitext(ydl.prepare_filename(temp))[0] + ".mp3"

    return (result)

def postprocess(src, dest_dir = _DEFAULT_OUTPUT):
    """
    Calls ffmpeg and removes scilences
    """
    def shellquote(s):
        return "'" + s.replace("'", "'\\''") + "'"

    #src = shellquote(src)
    #dest_dir = shellquote(dest_dir)
    destination = os.path.join(dest_dir, os.path.basename(src))
    ffmpeg = 'ffmpeg -i "' + src + '" -af silenceremove=1:0:-50dB "' + destination + '"'
    os.system(ffmpeg)
    os.system("rm " + src)

    return (destination)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        res = download(sys.argv[1])
        print (res)
        res = postprocess(res)
        print (res)
