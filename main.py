from pyicloud import PyiCloudService
from pwinput import pwinput
import json
import os

# other modules
from auth import auth
from download import download_photos

# get config variables
with open("config.json", "r") as f:
    config = json.load(f)

# sign in to icloud
# api = auth(os.getenv('ICLOUD_USER'), os.getenv('ICLOUD_PASSWORD'))

icloud_user = input("Please enter your iCloud username:" )
icloud_pass = pwinput("Please enter your iCloud password: ")
api = auth(icloud_user, icloud_pass)

# download photos
download_photos(api, config["download_target"], redownload_all=config["redownload_all"])