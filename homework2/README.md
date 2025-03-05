# Homework 2
This app allows a user to book seats for a movie that is showing. The user can also see their booking history that displays their booked movie seats.

# Project Structure
The <i>homework2</i> folder contains all needed files:
- The <i>movie_theater_booking</i> folder contains the app titled <i>bookings</i>.
    - Inside the <i>bookings</i> folder are Django's automatically generated files for its MVT structure -- models, tests, admin, urls, views, and templates.
- The <i>mysite</i> folder contains the settings for the Django project.
- The <i>myenv</i> is the virtual environment created for this webapp to run. It contains all the downloaded libraries needed.
- The <i>static</i> folder contains css styles that help contribute to the app's UI.

# Setup
<p>This project was set up using the instructions provided. Namely, I created a python virtual environment with the tag --system-site-packages. 
I installed django djangorestframework, as well as bootstrap. Then I ran django commands to start a new Django project:</p>
<p>django-admin startproject mysite movie_theater_booking
(this automatically generated the files inside mysite, namely settings, urls, etc)</p>
<p>Then, I created the bookings app:</p>
python manage.py startapp bookings
(this automatically generated the files inside bookings, namely admin, apps, models, test, views, migrations)

# How to Run
1) cd to /home/student/cs4300/homework2
2) activate virtual environment source myenv/bin/activate
3) cd movie_theater_booking
4) run server - python manage.py runserver 0.0.0.0:3000
5) click app button on devedu page

# How to Test
1) cd to /home/student/cs4300/homework2
2) activate virtual environment source myenv/bin/activate
3) cd movie_theater_booking
4) run tests - python manage.py test (there are 14 tests in total) 
   
