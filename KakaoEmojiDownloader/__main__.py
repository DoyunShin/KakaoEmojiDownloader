import KakaoEmojiDownloader as ked
from pathlib import Path
import click

__version__ = "1.0.0"

@click.version_option(prog_name="KakaoEmojiDownloader", version=__version__)

@click.command()
@click.option("--debug", is_flag=True, help="Enable debug mode")
@click.option("--slug", required=False, default=None, help="Slug of the emoji")
@click.option("--thread", required=False, default=4, help="Number of threads")
def main(debug, slug, thread):
    """
    Start the downloader
    """
    if debug:
        ked.logger.setLevel("DEBUG")
    ked.downloader.THREAD = thread
    if slug:
        ked.download(slug)
        exit(0)
    
    while True:
        print("Please enter the URL of the KakaoTalk emoji you want to download.")
        slug = input("URL: ")
        if slug == "exit":
            break
        if slug.startswith("http"):
            slug = slug.split("/")[-1]
        ked.logger.info(f"Downloading {slug}...")
        ked.downloader.download(slug)


if __name__ == "__main__":
    main()
