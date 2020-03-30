#!/usr/bin/python3

import requests
import urllib
import re

url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=10&mkt=en-IN"

resRaw = requests.get(url)
res = resRaw.json()
for image in res['images']:
    url = f"https://bing.com/{image['url']}"
    reSearch = re.search('id=(.+?)&', url)
    if reSearch:
        imageName = reSearch.group(1)
    else:
        imageName = f"{image['title'].replace(' ', '_').lower()}.jpg"
    imageRes = requests.get(url)
    with open(f"walls/{imageName}", 'wb') as f:
        f.write(imageRes.content)
        print(f"downloaded {imageName}")
