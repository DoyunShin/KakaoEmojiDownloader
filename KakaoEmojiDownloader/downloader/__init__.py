import KakaoEmojiDownloader as ked
from threading import Thread
from pathlib import Path
from time import sleep
import requests

THREAD = 4
downloadPath = Path("download/")
downloadPath.mkdir(exist_ok=True)
threads = {}

def download(slug):
    url = f"https://e.kakao.com/api/v1/items/t/{slug}"
    r = requests.get(url).json()

    name = r["result"]["title"]
    slug = r["result"]["titleUrl"]
    items = r["result"]["thumbnailUrls"]
    downFolderPath = downloadPath / slug
    downFolderPath.mkdir(exist_ok=True)
    ked.logger.info(f"Downloading {len(items)} emojis...")
    for item in items:
        filename = item.split("/")[-1]
        downPath = downFolderPath / (filename[32:]+".png")
        if downPath.exists():
            continue
        while True:
            if len(threads) < THREAD:
                t = Thread(target=download_item, args=(item, downPath))
                t.daemon = True
                t.start()
                threads[item] = t
                break
            sleep(0.1)

    while len(threads) > 0:
        sleep(0.1)
    print("Download complete!")
    pass

def download_item(url, path: Path):
    item = requests.get(url).content
    path.write_bytes(item)
    ked.logger.debug(f"Downloaded {path}")
    del threads[url]
    


