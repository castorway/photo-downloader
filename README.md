# photo-downloader

Script to automatically download all the photos from an iCloud drive to a filesystem. For those moving from iCloud to local storage for photos.

## Usage

Set the download target directory in `config.json`. Photos will be downloaded into subdirectories of this directory, labelled by year and month. For example, if `~/Photos` is the target directory, photos will be downloaded like this:

* `~/Photos`
  * `2024/`
    * `08/`
      * `image1.png`
      * `image2.png`
    * `07/`
    * ...
  * `2023/`
    * `12/`
    * `11/`
    * ...

Any files in `.heic` format will automatically be converted to `.png` format.

## Config

`download_target` is the target directory to which photos will be downloaded.

`redownload_all`, if set to `true`, will cause all photos to be redownloaded/replaced if a photo with the same name exists in iCloud. If set to `false`, photos with the same name as an existing photo are ignored.