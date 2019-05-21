#!/usr/bin/python3

import os
import requests
import logging
from fetch_spacex import download_picture

def fetch_hubble_pictures(url):
    response = requests.get(url)
    list_of_ids = [link['id'] for link in response.json()]
    logging.basicConfig(level = logging.DEBUG, filename = u'hubblelog.log')
    for id in list_of_ids:
        url = 'http://hubblesite.org/api/v3/image/{}'.format(id)
        response = requests.get(url)
        link = response.json()['image_files'][-1]['file_url']
        filename = '{}{}'.format(id, os.path.splitext(link)[-1])
        download_picture(link, filename)
        logging.info(u'Picture {} downloaded... Downloading next picture'.format(id))

if __name__ == '__main__':
    link = 'http://hubblesite.org/api/v3/images/wallpaper'
    fetch_hubble_pictures(link)