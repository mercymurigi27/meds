# MedAPP

>[mercy murigi](https://github.com/mercymurigi27/neighbohood.git)  
  
# Description  
this a medical record app that allows the user to have all their medical record saved together in case of an emergency
##  Live Link  
 
  

## User Story  
  
* Sign in with the application to start using.
* Set up a profile about me and add the dependancies ans their relation
* update each dependancies profile after each hosptial visit
* Find Contact Information for the next of kin or emergency contact person.
* add or remove dependancies
* Only view details of a single dependancy profile.
  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/mercymurigi27/neighbohood.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd MedAPP
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations hood
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
 
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 4.0.4](https://docs.djangoproject.com/en/4.4/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [mercymurigi41@gmail.com]  
  
## License 

* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)]  
* Copyright (c) 2022 **Mercy Murigi**
