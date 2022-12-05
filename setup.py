import setuptools
import re

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("KakaoEmojiDownloader/__main__.py", "r") as fh:
    version = re.search(r'__version__ = "(.*)"', fh.read()).group(1)

with open("requirements.txt", "r") as fh:
    install_requires = fh.read().splitlines()

setuptools.setup(
    name="KakaoEmojiDownloader",
    version=version,
    author="DoyunShin",
    author_email="doyun.shin@gmail.com",
    description="TDB Record Admin",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5.0",
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "ked = KakaoEmojiDownloader.__main__:main",
        ]
    },
)
