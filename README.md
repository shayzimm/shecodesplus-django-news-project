# Shay Zimmerle - She Codes News Project

## About This Project
A news site using Django that allows users to create their own accounts, write their own stories, and view the stories of other users.

Starter code for the Plus Django project can be found in the Plus Resources: Django Project Starter

## How To Run This Code
FYI the following instructions are for MAC

- Clone repo

- Create virtual environment (venv)

    `python -m venv venv`

- Initialise repo

    `git init`

- Activate venv

    `source .venv/bin/activate`

- Download the requirements

    `python -m pip install -r requirements.txt`

- Migrate the database

    `python manage.py loaddata news`

- Run server

    `python manage.py runserver`

## Database Schema
![Image of database schema](ERD.png)

## Project Features

- [x] Order the stories by date

- [x] Styled new story form

- [x] Story images

- [x] Login/Logout

- [X] Account view page

- [x] Create Account page

- [x] View stories by author

- [x] "Log-in" button only visible when no user is logged in/"Log-out" buttononly visible when a user *is* logged in

- [x] "Create Story" functionality only available when user is logged in

## Additional Features

- [x] Add the ability to update and delete stories (consider permissions - whoshould be allowed to update or and/or delete stories).

- [ ] Add categories to the stories and allow the user to search for stories by category.

- [ ] Add the ability to “favourite” stories and see a page with your favouritestories.

- [ ] Automatically publish stories on the day they are created, rather than allowing users to select a date.

- [x] Gracefully handle the error where someone tries to create a new story when they are not logged in.

#### Future Developments:

Here are some features yet to be implemented:
* Allow users to delete their accounts
* Search/filter by story categories
* Allow users to favourite stories ie. 'likes'
* Keyword Search
