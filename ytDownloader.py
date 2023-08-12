from pytube import YouTube
from pathlib import Path
default_path = str(Path.home() / "Downloads")

def download_vid(link, folder=default_path):
    """
    link - a web link, should be a YouTube link
    folder - a folder to which to download
    """
    # print(link)
    # if "https://www.youtube.com/" not in link and link != "https://www.youtube.com":
    #     print("Not a Youtube Video Link")
    #     return
    try:
        yt = YouTube(link)
        yd = yt.streams.get_highest_resolution()
        yd.download(folder)
    except:
        pass
    


    #print("title: ", yt.title)


if __name__ == "__main__":
    link = "https://www.youtube.com/watch?v=yWU8ynQ_tKs"
    download_vid(link)

