"""
Main script to run and download all opened Youtube tabs
It downloads them to the default download folder
"""
import ytDownloader
import getLinks

def main():
    url_list = getLinks.get_chrome_tabs()
    for link in url_list:
        ytDownloader.download_vid(link)
    
    print("Done")

if __name__ == "__main__":
    main()
