import os
from pathlib import Path
from tqdm import tqdm
import datetime


def download_photos(api, photo_dir, sort_method='month', redownload_all=False):
    '''
    Download all photos in the iCloud library and sort.

    Sort methods:
    - month: Photos are sorted into directories named YY-MM.
    '''

    album = api.photos.all

    top_path = Path(photo_dir)
    
    # iterate through all album photos and download
    for photo in tqdm(api.photos.all):

        # get path to download file
        dt = photo.added_date
        download_path = top_path / f'{dt.year:04}/{dt.month:02}'
        download_file = download_path / photo.filename

        if not redownload_all:
            # if file already exists in file structure, don't redownload it        
            if os.path.exists(download_file):
                continue
        
        # download and write file to directory

        download = photo.download()
        os.makedirs(download_path, exist_ok=True) # create any necessary directories if missing

        with open(download_file, 'wb') as f:
            f.write(download.raw.read())