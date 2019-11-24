# Reviewer
This is a clone of AWWARDS website which recognize and promote the talent and effort of the best developers, designers and web agencies in the world.

## Screenshots 
###### Home page
 
<img src="https://github.com/AliKheirAbdi/reviewer/blob/master/reviews.png"> 

## User Story  
  
* View posted projects and their details
* Post a project to be rated/reviewed
* Rate/ review other users' projects
* Search for projects 
* View projects overall score
* View my profile page
  
  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/AliKheirAbdi/reviewer.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Reviewer pip install -r requirements.txt 
```
##### Install and activate Virtual Env
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  On your database setup User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations
 ``` 
 Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
Open the application on your browser `127.0.0.1:8000`.  

## BDD
| Input        | Output           | Behavior  |
| ------------- |:-------------:| -----:|
| Register      | Fill out the reg form | user is created |
| Login     | Enter username and pwd   | Application logs user in |
| Edit Profile | User fills out biodata and photo | Profile is created|
| Share project|pop up for user to upload images | User can edit,caption photo|
| Rate photo|click on stars to rate project 1-10| button click|
  
## Technology used  
  
* [Python3.7](https://www.python.org/)  
* [Django 2.2](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com) 
* [Javascript]
  
## Known Bugs  
* There are currently no known bugs.  
  
## Contact Information   
If you are interested in this project or making contributions, please email me at [akheirali(@)gmail.com]  
  
## License 
 MIT License
*Copyright (c) 2019 **Ali Kheir**
