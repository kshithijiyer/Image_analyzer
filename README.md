# Image Analyzer
This is a Django application which uses Google's Vision API to analyze images and show results on an web browser.

## Prerequisites
1. Google cloud API key
2. Python 2.x
3. Django 1.x

## Installation and Execution
1. Download the project files from github.
```
git clone https://github.com/kshithijiyer/Image_analyzer.git
```
2. Set the path to apikey.json file.
```
export GOOGLE_APPLICATION_CREDENTIALS=/path/api.json
```
3. Change directory to the project directory 
```
cd Image_analyzer
```
4. Now start the django server.
```
python manage.py runserver
```
5. Open the link ```http://127.0.0.1:8000/analyze/``` on your web-browser to use the Application.

## Usage
* Click on ```select some files``` button and select any  ```*.jpg``` file.
* Now click on ```Submit``` button.
* Click on ```History``` button to get an history of all the images analyzed.

## Built with 
1. [Pycharm](https://www.jetbrains.com/pycharm/download/)
2. [Django](https://www.djangoproject.com/download/)
3. [Python](https://www.python.org/downloads/)

## Author
[Kshithij Iyer](https://www.linkedin.com/in/kshithij-iyer/)

## Licence 
The project is released under apache 2.0 licence.

