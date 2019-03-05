# Photoapp

A python app that lets one to see a gallery with photos with their descriptions


#### Date of Current Version (March 5th,2019)
#### By **Joy Wendo**
## Description
This is a Django application which allows users to view photos which can be filtered into their different categories and locations.
Try it out : <https://joygallery.herokuapp.com/>
## Prerequisites
You need the following to work on the project: -
* Python version 3.6 
* Pip 
* venv 
* A text Editor(vscode preferably)
## Setup/Installation Requirements
* To start using this project use the following commands:
```bash
$ git clone https://github.com/joyjoie/photoapp
```
```bash
$ cd Blog
```
* create a virtual environment
```bash
$ python3.6 -m venv virtual
```
* navigate into the virtual environment
```bash
$ source virtual/bin/activate
```
* while in the Virtual environment install the dependencies found in the  requirements.txt file
```bash
(virtual)$ pip install -r requirements.txt
```
* create a .env file and in it input the following:
```bash
SECRET_KEY=''
DEBUG=True #Set To False in Production
DB_NAME='<Your DB Name>'
DB_USER='<Your DB Username>'
DB_PASSWORD='<Your DB Password>'
DB_HOST='127.0.0.1'
MODE='dev' #set to prod in production
ALLOWED_HOSTS=['*']
DISABLE_COLLECTSTATIC=1
```
* add the .env file into the .gitignore
* create a database called photo
```bash
(virtual)$ psql
joy=# CREATE DATABASE photo;
```
* make migrations
```bash
(virtual)$ python3.6 manage.py makemigrations gallery
(virtual)$ python3.6 manage.py migrate
```
* to run the project enter this command
```bash
(virtual)$ python3.6 manage.py runserver
```
* access the application on this localhost address http://127.0.0.1:8000
## Behaviour Driven Development
|  Behaviour |  Input  |  Output |
|------------|---------|---------|
| Home | - | - |
|View Images| Click on View Image | A smaller image appears with the image name, description and date published|
|Search | Nature | Images in the Nature category are Displayed |

## Link to Live Website 
Here is a link to the live website: <https://joygallery.herokuapp.com/>
## Known Bugs
None known at the moment.
## Technologies Used
* HTML
* JavaScript
* CSS
* Python
## License
MIT License
Copyright (c) 2019 Joy Wendo