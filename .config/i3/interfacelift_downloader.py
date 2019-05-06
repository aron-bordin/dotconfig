#!/usr/bin/python3
from __future__ import print_function
from urllib.request import urlopen, Request
import queue

import os
import sys
import re
import threading
import time
import argparse
import shutil
import subprocess
import random

# Merge dictionaries. Used for merging resolutions.
# Necessary workaround for Python 2.x   :(


def merge_dicts(*dict_args):
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


HOST = 'http://interfacelift.com'
RES_WIDESCREEN_16_9 = {
    # widescreen 16:9
    '5120x2880': '/wallpaper/downloads/date/wide_16:9/5120x2880/',
    '3840x2160': '/wallpaper/downloads/date/wide_16:9/3840x2160/',
    '3200x1800': '/wallpaper/downloads/date/wide_16:9/3200x1800/',
    '2880x1620': '/wallpaper/downloads/date/wide_16:9/2880x1620/',
    '2560x1440': '/wallpaper/downloads/date/wide_16:9/2560x1440/',
    '1920x1080': '/wallpaper/downloads/date/wide_16:9/1920x1080/',
    '1600x900': '/wallpaper/downloads/date/wide_16:9/1600x900/',
    '1366x768': '/wallpaper/downloads/date/wide_16:9/1366x768/',
    '1280x720': '/wallpaper/downloads/date/wide_16:9/1280x720/',
}

IMG_PATH_PATTERN = re.compile(r'<a href=\"(?P<path>.+)\"><img.+?src=\"/img_NEW/button_download')
IMG_FILE_PATTERN = re.compile(r'[^/]*$')

# Downloads the given url and write it to the given directory


def download_file(url, saveDir):
    # interfacelift returns a 403 forbidden unless you include a referer.
    headers = {'User-Agent': "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)", 'Referer': url}
    req = Request(url, None, headers)
    filename = IMG_FILE_PATTERN.search(url).group()
    saveFile = os.path.join(saveDir, filename)
    with open(saveFile, 'wb') as f:
        try:
            res = urlopen(req)
            f.write(res.read())
            print('[+] Downloaded %s' % filename)
            subprocess.run(['feh', '--bg-max', saveFile])
        except Exception as e:
            print(e)
            try:
                os.remove(saveFile)
            except:
                pass


# Returns the path of the specified page number
def get_page_path(pageNumber):
    return '%sindex%d.html' % (RES_PATH, pageNumber)

# Returns the full URL of the specified path
def get_url_from_path(path):
    return '%s/%s' % (HOST, path)

# Returns the full URL of the specified page number
def get_page_url(pageNumber):
    return get_url_from_path(get_page_path(pageNumber))

# Opens the specified page and returns the page's HTML content
def open_page(pageNumber):
    url = get_page_url(pageNumber)
    # interfacelift returns a 403 forbidden unless you include a referer.
    headers = { 'User-Agent' : "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)",
                'Referer': url}
    try:
        req = Request(url, None, headers)
        f = urlopen(req)
    except IOError as e:
        print('Failed to open', url)
        if hasattr(e, 'code'):
            print('Error code:', e.code)
    return f.read().decode(errors='ignore')

# Returns the specified number of seconds in H:MM:SS format
def pretty_time(seconds):
    m, s = divmod(round(seconds), 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)


SAVE_DIR = '/tmp/wallpapers'
RES_PATH = '/wallpaper/downloads/date/wide_16:9/1920x1080/'

# Create directory if not exist
os.makedirs(SAVE_DIR, exist_ok=True)

timeStart = time.time()

# Add image URLs to queue
page = random.randint(1, 300)
count = 0

while True:
    pageContent = open_page(page)
    links = list(IMG_PATH_PATTERN.finditer(pageContent))
    link = random.choice(links)
    url = get_url_from_path(link.group('path'))
    filename = IMG_FILE_PATTERN.search(url).group()
    saveFile = os.path.join(SAVE_DIR, filename)

    if not os.path.isfile(saveFile):
        download_file(url, SAVE_DIR)
        count += 1
        break
    else:
        print('[-] Skipped %s (already exists)' % filename)
        continue


print('[*] Download finished! (%d files)' % count)
print('[*] Time taken: %s' % pretty_time(time.time() - timeStart))
