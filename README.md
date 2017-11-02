# Small python scripts

## [song-manager.py](https://github.com/TarlyFM/small_scripts/blob/master/song_manager.py)

### Goal

- [x] Downloads an audio file if necessary from a server : [YouTube](https://www.youtube.com)
- [ ] Download from (s)ftp
- [x] Trims silences at the beginning and ending of the audio file with [ffmpeg](https://github.com/FFmpeg/FFmpeg)
- [ ] Tries to complete metadata with [DiscogsTagger](https://github.com/jesseward/discogstagger)
- [x] Stores the file in $HOME/Music

### Params

* URI or absolute path
* Optionnal: another function to be called with the absolute path

### Install latest version
`pip install -e git+https://github.com/UDONRadio/UDON_scripts.git@master#egg=UDON_scripts`

### Modules required

* [youtube-dl](https://github.com/rg3/youtube-dl)
* [ffmpeg-python](https://github.com/kkroening/ffmpeg-python)
* [DiscogsTagger](https://github.com/jesseward/discogstagger)
* [eyeD3](https://github.com/nicfit/eyeD3)
