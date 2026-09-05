from core import CoreYTDLP

class YoutubeDownload(CoreYTDLP):
    def setToDownloadMode(self, audioFormat: str):
        postProcess = {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': audioFormat
        }
        
        if audioFormat == 'mp3':
            postProcess['preferredquality'] = '192'
            
        self.yt_opt = {
            'postprocessors': [postProcess],
            'quiet': True,
            'format': 'bestaudio',
            'ffmpeg_location': './ffmpeg_bin/ffmpeg',
            'outtmpl': './output/%(title)s.%(ext)s',
            'extract_flat': False,
            'socket_timeout': 40
        }
    
    def setToExtractorMode(self, fastQuery: bool):
        e = 'in_playlist' if fastQuery else False
        
        self.yt_opt = {
            'quiet': True,
            'verbose': False,
            'extract_flat': e # Fast query search, only return flat content
        }
        
    def setURL(self, url):
        self.yt_url = url
    
    def setOptions(self, opt):
        self.yt_opt = opt
    
    