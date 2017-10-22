"""
Song manager

Ensure downloading, cleaning and storing songs.
"""
import youtube_dl

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'aac',
        'preferredquality': '320',
    }],
    'logger': MyLogger(),
}

def downloader(link, callback, **args):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
