# Social-OAuth
Task for Web Club || Implementing Sign In via Google,GitHub
# Task Id :Google/Facebook/Github_Auth

# Framework/Language used : 
Django,HTML,CSS,Bootstrap,JavaScript


# Instructions :

Procedure to run:

1) Create virtual environment.
   ```python3 -m venv myvenv```
   ```source myvenv/bin/activate```
2) Install require packages in virtual environment using requirements.txt
   ```pip3 install -r requirements.txt```
3) Then makemigrations and migrate
   ```python3 manage.py makemigrations ```
   ```python3 manage.py migrate```
4) Finally runserver
   ```python3 manage.py runserver```
  
  For deploying on local server:
  
  To Sign in through Google ,you can use any of the following urls:
  http://127.0.0.1:8000/
  
  localhost:8000/
  
  To Sign In Through GitHub use the following url in your browser:
  localhost:8000/
  
  # Extra work done:
  Service Worker file has been added,
  It can be used as a Progressive Web App if we install site assets
  
  # Django Authentication (sign in/sign up)
  There is code for django authentication also .There is an app called Account where we can find the code. But the urls have not been     included in root urls.py 
  
  Also there is an app called blog where we can post blogs.Even this app's url has not been included in the root urls.py
  
