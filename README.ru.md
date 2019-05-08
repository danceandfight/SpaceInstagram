# Космический Инстаграм

Проект "Космический инстаграм" состоит из трех модулей:
* fetch_spacex - позволяет скачивать фотографии с сайта spacex, через [spacex api](https://documenter.getpostman.com/view/2025350/RWaEzAiG#bc65ba60-decf-4289-bb04-4ca9df01b9c1).

* fetch_hubble - позволяет скачивать фотографии с сайта hubble, через [hubble api](http://hubblesite.org/api/documentation).

* post_on_instagram - позволяет загружать фотографии в инстаграм с помощью instabot

### Как установить

* fetch_spacex: С помощью api spacex найдите интересующий вас запуск, например, последний https://api.spacexdata.com/v3/launches/latest и передайте ссылку функции `fetch_spacex_last_launch()`.

* fetch_hubble: С помощью api hubble выберите интесующую вас коллекцию фотографий, например, http://hubblesite.org/api/v3/images/wallpaper и передайте ссылку функции `fetch_hubble_pictures()`
Оба модуля скачивают фотографии в общую папку `images`.

* post_on_instagram: собирает все фотографии из папки `images`, сортирует их по названию и постит в инстаграм

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).