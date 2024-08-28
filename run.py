from pyicloud import PyiCloudService
from pwinput import pwinput
import json

from modules.auth import auth
from modules.download import download_photos

# get config
with open("config.json", "r") as f:
    config = json.load(f)

# code for credentials stored in .env for testing purposes
# import os
# api = auth(os.getenv('ICLOUD_USER'), os.getenv('ICLOUD_PASSWORD'))

# sign in to icloud
icloud_user = input("Please enter your iCloud username: ")
icloud_pass = pwinput("Please enter your iCloud password: ")
api = auth(icloud_user, icloud_pass)

print("Authenticated! Downloading photos...")

# download photos
download_photos(api, config["download_target"], redownload_all=config["redownload_all"])