import yt_dlp
from yt_dlp.utils import DownloadError, ExtractorError, DownloadCancelled 

broken_extractor = []

class CoreYTDLP:
    def __init__(self, opt: dict, url: list):
        self.yt_opt = opt
        self.yt_url = url

    def extract(self):
        with yt_dlp.YoutubeDL(self.yt_opt) as ydl:
            try:
                data = ydl.extract_info(url=self.yt_url[0], download=False)
                return ydl.sanitize_info(data)
            
            except ExtractorError:
                raise ExtractorError('Error Extractor')
            
    def extractByName(self, name: str, count: int):
        with yt_dlp.YoutubeDL(self.yt_opt) as ydl:
            try:
                query = f"ytsearch{count}:{name}"
                data = ydl.extract_info(url=query, download=False)
                return ydl.sanitize_info(data)
            except ExtractorError:
                raise ExtractorError('Error Extractor')

    def getAllExtractorOptions(self):
        ext_list = yt_dlp.gen_extractors()
        return ext_list

    def checkExtractor(self):
        extractors = self.getAllExtractorOptions()
        for extractor in extractors:
            if extractor.working():
                if extractor.suitable(self.yt_url[0]):
                    pass
                else:
                    global broken_extractor
                    broken_extractor.append(extractor.IE_NAME)
        return broken_extractor

    def Download(self):
        with yt_dlp.YoutubeDL(self.yt_opt) as ydl:
            try:
                ydl.download(self.yt_url)

            except DownloadCancelled:
                return DownloadCancelled.msg

            except DownloadError:
                raise ValueError(DownloadError.msg)
        
