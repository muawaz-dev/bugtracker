#  BugTracker – Django Web Application

##  Overview
BugTracker is a full-stack web application built with Django that allows users to report and track bugs related to an FPS game. It features user authentication, bug submission, and personalized dashboards. This project demonstrates core backend development skills including form handling, user authentication and database integration.

---

##  Features

-  User registration, login, logout, and password reset
-  Bug reporting with title, description,number of occurences
-  Account page displaying user details and their submitted bugs
-  Admin interface for managing users and bugs

---

##  Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (AI assisted)
- **Database**: SQLite (default, easily swappable)
- **Authentication**: Django’s built-in auth system

---

##  Installation & Setup
- Clone the repo
git clone https://github.com/muawaz-dev/bugtracker.git
- In terminal:cd bugtracker

- Create virtual environment
python -m venv venv
- source venv/bin/activate  # or venv\Scripts\activate on Windows

- Install dependencies
pip install -r requirements.txt

- Run migrations
python manage.py migrate

- Start the server
python manage.py runserver

