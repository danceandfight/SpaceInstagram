#!/usr/bin/python3

import os
from instabot import Bot

def get_pictures_list():
    pics = sorted(os.listdir('./images'))
    pics = filter(lambda x: x.endswith('.jpg'), pics)
    return pics

def get_posted_pictures_list():
    try:
        with open('pics.txt', 'r', encoding='utf8') as f:
            posted_pics_list = f.read().splitlines()
    except FileNotFoundError:
        posted_pics_list = []
    return posted_pics_list

def update_posted_pictures_list(pic, posted_pics_list):
    posted_pics_list.append(pic)
    with open('pics.txt', 'a', encoding='utf8') as file:
        file.write(pic + '\n')

def post_photo(photo):
    bot = Bot()
    bot.login()
    file_with_path = './images/{}'.format(photo)
    caption = photo.split('.')[0]
    bot.upload_photo(file_with_path, caption=caption)
    
def main():
    list_of_photos = get_pictures_list()
    posted_photos = get_posted_pictures_list()
    for pic in list_of_photos:
        if pic not in posted_photos:
            post_photo(pic)
            update_posted_pictures_list(pic, posted_photos)


   
if __name__ == '__main__':
    main()
