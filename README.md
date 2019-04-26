# si507 Final Project

Song Generator Project
https://github.com/amyamyc/si507-final-project-itunes

---

## Project Description

This project utilizes the itunes API. Through the API, the project extracts several music genres information from itunes. Based on genre selected by user, the program will provide user with songs from that genre.

## How to run

1. First, you should install all requirements by locating project folder and typing in `pip install -r requirements.txt` in the terminal.
2. Second, you should run the file by typing "python app.py runserver" into terminal. After this, the terminal should populate with a link ending in the numbers "5000"
3. In order to see the user interface, paste this link into your web browser.
4. Please note: Alternatively, if installing the requirements causes package errors in the terminal which causes the local host link to be broken, you can utilize the virtual environment provided in repository. Please activate the virtual environment called "project1env" and type in "python app.py runserver".

## How to use
1. User can input one of these three music genres into the Route 3 (See below in Routes section). Genres that can be inputted are "Pop", "Country", "Hip-Hop". Please include capitalization as shown when inputting the genre in the route.
2. Alternatively, users can also click on the links on the interface to go see the songs from the desired genre.

## Routes in this application
- Route 1: / →   
  This page will read "Hello!! There are 96 Songs saved in your database." Below the sentence are 5 links that will bring you to various pages with specified song. For example, the link labeled "See all Pop Songs" will bring you to a page with only the songs from the Pop genre.

- Route 2: /all_songs →   
  This page will the title and artist of all the songs in your database.

- Route 3: /songs/<Genre> →   
  This is the songs generator. This route will populate a list of songs from the genre that is inputted by the user.

## How to run tests
Sorry! I was not able to create test files.

## In this repository:
- si507-final-project-itunes (repository name)
- app.py
- db.py
- SI507_project_tools.py
- models.py
- sample.db
- requirements.txt
- database_schema.jpg
- example_cache.json
- project1env folder (virtual environment)
- Screenshots folder (contains 3 screenshots of how site should render for user)
- Templates folder
  - index.html
  - all_songs.html
  - genre.html

---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
- [ ] This is a completed requirement.
- [x] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [x] Project is submitted as a Github repository
- [x] Project includes a working Flask application that runs locally on a computer
- [ ] Project includes at least 1 test suite file with reasonable tests in it.
- [x] Includes a `requirements.txt` file containing all required modules to run program
- [x] Includes a clear and readable README.md that follows this template
- [x] Includes a sample .sqlite/.db file
- [x] Includes a diagram of your database schema
- [x] Includes EVERY file needed in order to run the project
- [x] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [x] Includes at least 3 different routes
- [x] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [x] Interactions with a database that has at least 2 tables
- [x] At least 1 relationship between 2 tables in database
- [x] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [ ] Use of a new module
- [ ] Use of a second new module
- [ ] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [ ] A many-to-many relationship in your database structure
- [ ] At least one form in your Flask application
- [x] Templating in your Flask application
- [x] Inclusion of JavaScript files in the application
- [x] Links in the views of Flask application page/s
- [ ] Relevant use of `itertools` and/or `collections`
- [ ] Sourcing of data using web scraping
- [x] Sourcing of data using web REST API requests
- [ ] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [x] Caching of data you continually retrieve from the internet in some way

### Submission
- [x] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [x] I included a summary of my project and how I thought it went **in my Canvas submission**!
