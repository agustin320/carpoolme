# README #

Carpool is an open source [carpooling](https://en.wikipedia.org/wiki/Carpool) proyect that arose of several atospheric issues that Mexico City is currently facing due to the saturation in the number of cars this city has. This project is intended to expedite the implementation of carpooling culture in any city to help minimze CO2 emissions by sharing a car with others that might have a similar commute route, this proyect will also give the ability to create and search routes based on origin and destination and getting in contact through Facebook for faster communication.  

### How do I get set up? ###
#### Deployment
First of start by deploying to heroku:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

#### Configuration
Once you have you app running, you have to apply the migrations and create a super user to access the Django admin interface and start adding the basic config stuff.
* ``` python carpool/manage.py migrate```
* ``` python carpool/manage.py createsuperuser```
* Access the admin interface on /admin path

##### Social Login Config:
* Add a Site for your domain, matching settings.SITE_ID (django.contrib.sites app)
* For each OAuth based provider, add a Social App (socialaccount app)
* Fill in the site and the OAuth app credentials obtained from the provider
* More info at: http://django-allauth.readthedocs.io/en/latest/installation.html

### Contribution guidelines ###

#### Branches
* ```master```: is the latest, deployed version, is not advised to make PRs against this branch
* ```develop```: is the preferred development branch for the next release, here's where all PRs should be made from.

#### Pull Requests
* Just make them from the ```develop``` branch and evrything should be ok
* for the moment we don't have any code review, test coverage, etc.

#### Coding Standards
* Python: https://www.python.org/dev/peps/pep-0008/

### Who do I talk to? ###

* Author: Agustin Ferrari (twitter:@agustin320)
