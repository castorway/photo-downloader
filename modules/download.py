import os
from pathlib import Path
from tqdm import tqdm
from modules.heic2png import convert_single_heic_to_png


def download_photos(api, photo_dir, redownload_all=False):
    '''
    Download all photos in the iCloud library and sort.
    '''

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

        # check if image needs to be converted from HEIC
        if str(download_file).lower().endswith(".heic"):
            convert_single_heic_to_png(str(download_file))