#!/usr/bin/python3

import requests
import os

def get_url_list(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['links']['flickr_images']
  
def download_picture(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    os.makedirs(os.path.abspath('.') + '/images', exist_ok=True)
    with open('images/' + filename, 'wb') as file:
        file.write(response.content)

def fetch_spacex_last_launch(url):
    list_of_links = get_url_list(url)
    for link_number, link in enumerate(list_of_links):
        filename = 'spacex{}.jpg'.format(link_number)
        download_picture(link, filename)

if __name__ == '__main__':
    link = 'https://api.spacexdata.com/v3/launches/76'
    fetch_spacex_last_launch(link)
