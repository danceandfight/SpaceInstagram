# Space Instagram

Space instagram project consist of three modules:

* fetch_spacex is for downloading images from spacex site via [spacex api](https://documenter.getpostman.com/view/2025350/RWaEzAiG#bc65ba60-decf-4289-bb04-4ca9df01b9c1).

* fetch_hubble is for downloading images from hubble site via [hubble api](http://hubblesite.org/api/documentation).

* post_on_instagram is for uploading photos to instagram.

### How to install

* fetch_spacex: use spacex api to find the photos of the launch you want to download, for example the latest launch https://api.spacexdata.com/v3/launches/latest and use it as an argument for `fetch_spacex_last_launch()` function.

* fetch_hubble: use hubble api to find a collection of photos you want to download, for example http://hubblesite.org/api/v3/images/wallpaper and use it as an argument for `fetch_hubble_pictures()` function.

These two modules downloads photos to the shared `image` folder.

* post_on_instagram: collects and sorts by name all photos in `image` folder and posts them on instagram

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
