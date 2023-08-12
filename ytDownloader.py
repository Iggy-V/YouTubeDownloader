from pytube import YouTube

def download_vid(link, folder):
    """
    link - a web link, should be a YouTube link
    folder - a folder to which to download
    """

    if "https://www.youtube.com/" not in link:
        print("Not a Youtube Link")
        return
    yt = YouTube(link)

    #print("title: ", yt.title)

    yd = yt.streams.get_highest_resolution()
    yd.download(folder)

    


