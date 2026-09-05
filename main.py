from youtube import YoutubeDownload

def MainMenu():
    ytdl = YoutubeDownload(
        opt={},
        url=[]
    )
    
    while True:
        ytdl.setToExtractorMode(fastQuery=True) # gen extractor options
        s_query = input("\nInput song name: ")
        info = ytdl.extractByName(s_query, 5)

        if 'entries' in info and len(info['entries']) > 0:
                
            print(f"We found {len(info['entries'])} matches with your search, please choose 1-{len(info['entries'])}:\n")
            
            for i in range(len(info['entries'])):
                print(f"{i + 1}. {info['entries'][i].get('title')}")
                
            chooseIndex = int(input("Choose: "))
            
            try:
                data = info['entries'][chooseIndex - 1]
                ytdl.setURL(data.get('url'))
                
                ytdl.setToDownloadMode(audioFormat='wav')
                ytdl.Download()
            except IndexError:
                raise IndexError(info['entries'][chooseIndex - 1])

        else:
            print(f"can't found exact song: {s_query}")

if __name__ == "__main__":
    MainMenu()
