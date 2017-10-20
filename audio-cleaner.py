import urllib
import youtube_dl
import re
import os
from subprocess import call

def mabite(link, f = None, *args):
    downloaded = False;
    fname = ""

    if re.match("^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$", link) is not None:
        call(["youtube-dl", "-x", link])
        downloaded = True

    if re.match("^s?ftp://([a-z0-9]+:[a-z0-9]+@)?([\\.a-z0-9]+)/([\\./a-z0-9]+)$", link) is not None:
        urllib.urlretrieve(link, os.path.basename(link))
        downloaded = True

    if not downloaded:
        return -1
