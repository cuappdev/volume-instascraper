# volume-instascraper
[![Python 3.9.12](https://img.shields.io/badge/python-3.9.12-blue.svg)](https://www.python.org/downloads/release/python-3912/)

Instagram web scraper for Cornell AppDev's Volume

Download images from public user posts on Instagram

## Installation
Clone the project with
```
$ git clone git@github.com:cuappdev/volume-instascraper.git
```
or
```
https://github.com/cuappdev/volume-instascraper.git
```

and install dependencies with
```
$ pip install -r requirements.txt
```
or
```
$ pip3 install -r requirements.txt
```

## How to use
1. Open `usernames.txt` and replace the placeholder values with the profile's <ins>username</ins>. Every username must be separated by a new line.
2. Run `python app.py` from the top level. If the command does not work, try `python3 app.py`.
3. Enter the start date. It must be in the format `m-d-yyyy`. For example, `4-4-2023` for April 4, 2023.
4. To cancel the downloads, press `CTRL + C` on your keyboard.
