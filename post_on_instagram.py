#!/usr/bin/python3

import os
from instabot import Bot

def main():
  posted_pic_list = []
  try:
    with open('pics.txt', 'r', encoding='utf8') as f:
      posted_pic_list = f.read().splitlines()
  except Exception:
    posted_pic_list = []

  bot = Bot()
  bot.login()
  pics = sorted(os.listdir('./images/*.jpg'))
  pics = filter(lambda x: x.endswith('.jpg'), pics)

  try:
    for pic in pics:
      if pic not in posted_pic_list:
        caption = pic.split('.')[0]
        bot.upload_photo(pic, caption=caption)
        posted_pic_list.append(pic)
        with open('pics.txt', 'a', encoding='utf8') as file:
          file.write(pic + '\n')
  except Exception as e:
    print(str(e))

if __name__ == '__main__':
  main()
  