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

def get_ydl_opts(dest):
    return {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'logger': MyLogger(),
        'outtmpl': dest + '%(title)s-%(id)s.%(ext)s',
        'progress_hooks': [my_hook],
        'noplaylist': True,
        'nocheckcertificate': True,
    }

def download(link, dest_dir=_DEFAULT_PATH):
    """
    Where the magic happens
    """
    result = ""

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    ydl_opts = get_ydl_opts(dest_dir)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
        temp = ydl.extract_info(link)
        result = os.path.splitext(ydl.prepare_filename(temp))[0] + ".mp3"

    return (result)

def postprocess(src, dest_dir=_DEFAULT_OUTPUT):
    """
    Calls ffmpeg and removes scilences
    """
    def shellquote(s):
        return "'" + s.replace("'", "'\\''") + "'"

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    destination = os.path.join(dest_dir, os.path.basename(src))
    ffmpeg = 'ffmpeg -y -i ' + shellquote(src) + ' -af silenceremove=1:0:-50dB ' + shellquote(destination)
    os.system(ffmpeg)
    os.system("rm " + shellquote(src))
    return (destination)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        res = download(sys.argv[1])
        print (res)
        res = postprocess(res)
        print (res)
