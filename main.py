from pyicloud import PyiCloudService
from dotenv import load_dotenv
import os
import sys

# other modules
from auth import auth
from download import download_photos

# get environment variables from .env file
load_dotenv()

# sign in to icloud
api = auth(os.getenv('ICLOUD_USER'), os.getenv('ICLOUD_PASSWORD'))

# download photos
download_photos(api, '/home/sintacks/Pictures/Album', redownload_all=True)