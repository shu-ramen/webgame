# webgame
Web Game Repository with Django and React

# Required Environments
## Python
* Python 3.6
* Django 2.1.7
* numpy  1.16.2
## Anaconda
* Latest Version (https://www.anaconda.com/)
## npm
* npm    5.6.0   (https://nodejs.org/ja/)

# To Run This App
```
$ git clone https://github.com/shu-ramen/webgame.git
$ conda activate [Your Django Environment]
$ cd src/webgame/react_jsx
$ npm install
$ cd ..
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver react
```