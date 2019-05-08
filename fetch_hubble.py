#!/usr/bin/python3

import requests
#from fetch_spacex import download_picture

def get_extension(url):
	return url.split('.')[-1]

def fetch_hubble_pictures(url):
	response = requests.get(url)
	list_of_ids = [link['id'] for link in response.json()] # example: [4001, 3995, ..., 3860]
	for id in list_of_ids:
		url = 'http://hubblesite.org/api/v3/image/{}'.format(id)
		response = requests.get(url)
		link = response.json()['image_files'][-1]['file_url']
		filename = '{}.{}'.format(id, get_extension(link))
		#download_picture(link, filename)
		print('Picture {} downloaded... Downloading next picture'.format(id))

if __name__ == '__main__':
	link = 'http://hubblesite.org/api/v3/images/wallpaper'
	fetch_hubble_pictures(link)