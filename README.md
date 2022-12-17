# My Chalet

![AmIResponsive](static/images/readme/amiresponsive.png)

## Introduction

My chalet is a fictional website designed for travel lovers. The purpose was to enhance user experience by gathering a list of the most exclusive chalets available in Italy. A user can quickly find the most requested and famous mini hotels, just by visiting the site and send a request for availability for one night stay.

## Live Site

Please find the live site [HERE](https://my-chalet.herokuapp.com/)

## Github Repository

The Repository can be found [HERE](https://github.com/aimansae/my-chalet)

## Table Of Contents
+ [Introduction](#introduction "Introduction")
    + [Live-site](#live-site "Live Site")
    + [Github-repository](#github-repository "Github Repository")
+ [UX](#ux "UX")
  + [Scope](#scope "Scope")      
  + [User Stories](#user-stories "User Stories")   
    + [First Time User](#as-a-first-time-user "As a first time user")   
    + [Existing User](#as-an-existing-user "As an existing user")  
    + [Admin](#as-a-site-creator-admin "As a site creator/admin") 
  + [Agile Methodology](#agile-methodology "Agile Methodology")
  + [Design](#design "Design")
    + [Wireframes](#wireframes "Wireframes")
    + [Database Schema](#database-schema "Database Schema") 
    + [Color Schema](#color-schema "Color Schema") 
    + [Fonts](#fonts "Fonts") 
+ [Features](#features "Features")
  + [Navbar](#Navbar "Navbar") 
  + [Footer](#footer "Footer")
  + [Login Page](#login-page "Login Page") 
  + [Fonts Page](#signup-page "Signup Page") 
  + [HomePage](#fonts "Fonts") 
  + [Description Page](#description-page "Description Page") 
  + [Reservation Page](#reservation-page "Reservation Page") 
  + [My Reservation Page](#my-reservations "My Reservations Page") 
  + [Edit Reservation ](#edit-reservation "Edit Reservation ") 
  + [Delete Reservation  ](#delete-reservation "Delete Reservation ") 
  + [Future Features](#future-features "Future Features") 
+ [Testing](#testing "Testing")
  + [Bugs](#bugs "Bugs")
  + [Technologies used](#technologies-used "Technologies used")
  + [Frameworks and libraries:](#frameworks-and-libraries: "Frameworks and libraries:")
  + [Additional Resources](#additional-resources "Additional Resources")
+ [Deployment](#deployment "Deployment")


## UX(User Experience)
<hr>

### Scope:

The overall purpose of the website is to spare users long researching online for the best chalet for a special occasion. Users should be able to find the best options available in the Country, in a timely manner,  by visiting the website and being able to consult details regarding the chosen option and ultimately send a reservation request directly from the website. Therefore the purpose is clear and immediate.

### [User Stories](https://github.com/users/aimansae/projects/5/views/1):

### As a first time user:

- I can [access](https://github.com/aimansae/my-chalet/issues/1) the website and see all the chalets the site has selected , ranked as the best ones. The site should be ituitive, immediate and provide all significant details about a chalet in the homepage.

- I can [choose](https://github.com/aimansae/my-chalet/issues/2) the chalet I like and read detailed information before submitting a reservation request. (*future features to be included here..*)

- I can [send](https://github.com/aimansae/my-chalet/issues/3) a reservation request selecting the desired date. (*future features to be included here..*)

- I can [register](https://github.com/aimansae/my-chalet/issues/4) so I can send a registraton request.

- I can [access](https://github.com/aimansae/my-chalet/issues/5) my reservations so that I can change or delete them

- I can [edit](https://github.com/aimansae/my-chalet/issues/6) my reservations so that I can change them.

- I can [delete](https://github.com/aimansae/my-chalet/issues/7) so I can remove a reservation request I submitted.



### As an existing user:

- I can log in to my exixting account, consult the requests I sent,  change or delete them.
- I can submit more reservation requests for the desired chalet

### As a site creator-admin:

- I want to be able to have access to all request users submitted
- I want to be able to delete or edit user requests
- I want all the data successfully stored in my internal database


### Agile Methodology

The development was made using the principles of agile methodology. User stories through github [Kanban](https://github.com/users/aimansae/projects/5) were created to ensure project delivery. Issues were prioritized using labels, must do and future features. All must have features were achieved successfully in a timely manner.

## Design

### Wireframes
Add flowchards and wireframes

### Database Schema
Add database schema

Database is created through 2 class based models:

ChaletList: presents the main details regardin all the chalet available. Currently there are 6 available options, containing chalet name , location, description, image and price info.

MakeReservation: contains a form requesing for user details in order to submit a reservation request: full name, email, phone, number of guests and date

### Color Schema

A background of black was used as main color to provide an elegant and fancy view and contrast all the eye-catching chalet images. 

### Fonts

The main font used is [Merriweather Sans](https://fonts.google.com/specimen/Merriweather+Sans)', while all main H1 headings are styled with [Raleway Font](https://fonts.google.com/specimen/Raleway). The selection is made to keep the elegant and modern look of the website.

## Features

### Navbar
The navbar is recurrent in all the pages. It contains the customized logo and links to navigate throught the page: Home, Login, Logout and My Reservation page, only if the user is authenticated.

If user is not logged in:

![Navbar](static/images/readme/navbar-no-login.png)

If user is logged in, login link will disappear from the navigation and Log out page will be shown instead:

![Navbar](static/images/readme/navbar.png)

### Footer
The footer is recurrent in all the pages as well. It contains links to social media for My Chalet website which open in a different tab.

![Footer](static/images/readme/footer.png)

### Login Page

Login page presents a form so existing users can insert their credentials and log in to send a reservaion request or consult the ones already submitted. 
If user doesn't have an account, they will be show a link that directs them to signup page

![Login-page](static/images/readme/login-page.png)


If user wants to logout a confirmation request will be shown, to confirm if the user wants actually to log out or return to the main page

![Logout-confirmation](static/images/readme/logout-confirmation.png)

### Sign Up Page

Sign up page allows a non existing user to create an account in order to send a requet for reservation. if they lready have an account a link is shown to direct them to login page.

FOTO

### Homepage 
The home page contains a small description specifying the purpose of the bage and appealing images showing all the 6 Chalets that were selected as the most wanted ones. Different images are present showing thechalets.
The user can click on button 'Reserve' an will be directed to another page showing more details regarding the selected chalet.

FOTOO

### Description Page
Once the user clicks on the desired chalet, a new page opens showig a detailed description and services the chalet offers, alonside with the price and a button to send a reservation request.
FOTOOOOO


### Reservation page

The reservation page form requires the user to insert their details and the date so that they can submit the request for reservation. For future feaures, the calendar will show the available dates and anfter sending the request a confirmation email will be sent to the user, ad a better ux experience.

![reservation-form](static/images/readme/reservation-form.png)

### My Reservation Page

For logged in users, my reservation page allows them to see all the reservation requests they sent. In addition to that users are able to change or delete a request.

![my-reservations](static/images/readme/my-reservations.png)

!!!!!!!TESTING
IF NO ACCOUNT: MESSAGE
!!!!!!!!!TESTING
If user doesnt have reservation requests, a message will be shown stating that there are no reservations.

### Edit Reservation 

If a user wants to change reservation, he can click on change and change the details as preferred. A confirmation message will be shown.

![change-reservations](static/images/readme/change-reservation.png)

### Delete Reservation 

A user is also able to delete their reservation and modal requesting double confirmation will be shown.

![delete-reservations](static/images/readme/delete-reservation.png)



## Future Features:

  - [Reservation confirmation](https://github.com/aimansae/my-chalet/issues/9): once selected the desired date, an email will be sent to the user regarding the availability.

  - [View more images](https://github.com/aimansae/my-chalet/issues/10): once the user will select click on a specific chalet to check the details, more images will be shown so they can consult the interior and all the services the structure provides.

  - [Consult Reviews](https://github.com/aimansae/my-chalet/issues/11): user will be able to check and post reviews regarding a specific chalet.

  - [Check Availability](https://github.com/aimansae/my-chalet/issues/12): while the user will be selecting the date a new calendar will appear showing availability for that specific date

  - [Overbooking/Double Booking](https://github.com/aimansae/my-chalet/issues/13): important feature to implement as the adming will be able to show information regarding double bookings, overbooking and in addition to that will implement code to limit the number of reservation requests a user van send.

  - Password Reset: a user will be able to reset their password, in case forgotten

  - prefill forms with data provided during registration process, so Users will not have to input the same data all the time. 

## Testing

## Bugs

## Technologies used

### [HTML5](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
### [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
### [Python v4](https://developer.mozilla.org/en-US/docs/Web/CSS)
### [Javascript](https://developer.mozilla.org/en-US/docs/Web/CSS)

## Frameworks and libraries:

- [Django](https://docs.djangoproject.com/en/4.1/): The app is built using Python Django Framework
- [Bootstrap 5](https://getbootstrap.com/): html pages styling and responsive design is achieved using bootstrap

## Additional Resources:
- Cloudinary database: used to store images
- [Baslamiq](https://balsamiq.com/): used for Wireframes
- Am I Responsive: for main picture showind responsivness on different devices

## Deployment

The site was created using [GitHub](https://github.com/). Here are the speps taken:

- Sign in to GitHub
- Code Institute Template was used by clicking on 'Use this template'
- Once the repo is created need to install Django and relevant libraries:

### Packages:

- pip3 install 'django<4' gunicorn
- pip3 install dj_database_url==0.5.0 psycopg2
- pip3 install dj3-cloudinary-storage
- pip3 install django-allauth
- pip3 freeze --local > requirements.txt
- django-admin startproject PROJ_NAME (my_chalet) . (dot to indicate we want to create the project in the current directory)
- python3 manage.py startapp APP_NAME ('my_chalet_site')

In setting.py file:
- in INSTALLED_APPS section: add  the APP_NAME with coma: 'my_chalet_site',

Need migrate the changes to the database by typing in terminal: 
- python3 manage.py migrate

To run the app type in terminal:
- python3 manage.py runserver
- opens site confirming 'Django app successfully created'

## Heroku Deployment and database

Create a database Heroku can access via ElephantSQL:

- Log in to [ElephantSQL.com](https://www.elephantsql.com/) to access your dashboard
- Click on “Create New Instance”
- Set up your plan
- Give the plan a Name (this is commonly the name of the project)
- Select the Tiny Turtle (Free) plan
- the Tags fields can be left blank
- click “Select Region”
- Select a data center near you
- Click on “Review”
- Verify your details and click “Create instance”
- In ElephantSQL dashboard  click on the database instance name for this project
- In the URL section, click the copy icon to copy the database URL(to be copied on Heroku Settings)


**In gitpod:**
- Create new env.py file on top level directory:  env.py
 - in this file add code 'import os'
- Set environment variables:
os.environ["DATABASE_URL"] = "Paste in  DATABASE_URL Link  from ElephantSQL "
- Add in secret key: 
os.environ["SECRET_KEY"] = "Make up your own randomSecretKey"
- type in terminal 'python3 manage.py migrate'

**In setting.py:** 
- connect env.py file by typing:

 import os
 import dj_database_url
 if os.path.isfile('env.py'):
     import env
- replace secret key with:
 SECRET_KEY = os.environ.get('SECRET_KEY')
- Comment out the original DATABASES variable and add:

 DATABASES = {
     'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
 }
- add Heroku to the ALLOWED_HOSTS in settings.py
- create Procfile withcode : web: gunicorn PROJ_NAME.wsgi


- save file and type:  python manage.py migrate

- commit and push the project to Github


- In ElephantSQL Dashboard:
- Click on 'Browser' tab on the left
- “Table queries” the list will be populated from your Django migrations.


The site is deployed to **Heroku** through the following steps:

- Log in to [Heroku](https://dashboard.heroku.com/apps) or create an account if required.
on home pace e click the button labelled 'New' in the top right corner
- From the drop-down menu select 'Create new app'.
- Choose a unique app name.
- Select the relevant geographical region.
- Click on 'Create App'.

- Go to 'Settings' tab and scroll down to the 'Config Vars' section.
- Click on 'Reveal Config Vars' and enter 'PORT' for the key and '8000' for the value. Then click 'Add'.
- Add CLOUDINARY_URL, DATABSE_URL and SECRET_KEY.

**Connect Heroku** to gitpod:

- Click on the 'Deploy' tab.
- Select as 'Deployment method': 'GitHub'.
- Search and Connect the relevant GitHub repository.
- Under 'Manual deploy' choose the correct branch and click 'Deploy Branch'.



