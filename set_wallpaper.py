#!/usr/bin/python3
from random import choice
import os
import json
import sys

configPath = os.path.join(os.getcwd(), 'config.json')
with open(configPath, 'r') as f:
    config = json.load(f)


images = [f for f in os.listdir('walls') if f != config['currentWallpaper']]
image = choice(images)
imageFullPath = os.path.join(os.getcwd(), f"walls/{image}")
print(imageFullPath)
cmd = f"gsettings set org.gnome.desktop.background picture-uri file:///{imageFullPath}"
print(f"executing {cmd}")
os.system(cmd)

config['currentWallpaper'] = image
with open(configPath, 'w') as f:
    json.dump(config, f)
