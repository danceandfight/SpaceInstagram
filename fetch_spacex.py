#!/usr/bin/python3

import requests
import os

def get_url_list(url):response = requests.get(url)
  return response.json()['links']['flickr_images']
  
def download_picture(url, filename):
  response = requests.get(url)
  try:
    os.makedirs(os.path.abspath('.') + '/images')
  except FileExistsError:
    pass
  with open('images/' + filename, 'wb') as file:
    file.write(response.content)

def fetch_spacex_last_launch(url):
  list_of_links = get_url_list(url)
  for link_number, link in enumerate(list_of_links):
    filename = 'spacex{}.jpg'.format(link_number)
    download_picture(link, filename)

if __name__ == '__main__':
  link = 'https://api.spacexdata.com/v3/launches/77'
  fetch_spacex_last_launch(link)
  