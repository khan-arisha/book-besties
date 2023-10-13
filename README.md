# cs257-s23-team-ks23
cs257-s23-team-ks23 created by GitHub Classroom

Project Title: 
Bombastic Book Besties

Authors:
- Arisha Khan: https://github.com/khan-arisha
- Sophie Quinn: https://github.com/quinns7
- Celia Vander Ploeg Fallon: https://github.com/celiavpf 
- Selma Vangstein: https://github.com/selmavangstein

all members of the Carleton College class of 2025

Project Description: 
This was our term-long/final project for CS257 Software Design in Spring 2023. We have created a database-driven website that focuses on NYT Hardcover Fiction Bestsellers between 1931 and 2020. We implemented this using Postgresql, Flask, Jinja, HTML, CSS, JS, and Python. We have functionality separated between the backend (API_web.py), frontend (web), and interpreter (webapp.py). We ran this through Carleton's remote Perlman server. In previous versions of this product, we had a CSV backend and a Command-Line Interface.

Future Fixes:
There was some functionality to the website that we wanted to add but were not able to implement with the time and resources available to us. Perhaps we will get this working in the future.
- We wanted searchable dropdown menus in queries such as Books by Author and Book Info. We tried to implement this with Select2, but it did not work. 
- We tried many different ways to center the tables, none of which worked consistenly. We also never came up with a great way to display some of the table results. 
- Some of the apostrophes and quotation marks don't encode correctly in our HTML, but we were not able to fix this.
- We wanted to fix some of the capitalization weirdness, such as capitalizing after apostrophes and numbers, but we were not able to find a solution to this problem.
- We had to create a copy of our API in our web folder because the Python accessing to the backend folder did not work. This left us with different versions of the API in different folders.
- When searching for information about books, we are unable to return information for books with the exact same title. This is due to the database query being based solely on book title and not book title and author in combination. This is a minor problem that comes up for only a select few books, but in the future we could write another function in the API to solve this problem.

Table of Contents:
- backend
    - API and Command-line interface client
    - unit tests for API
- data
    - CSV files that we created tables from
- web
    - static: all our CSS stylesheets
    - templates: all our HTML templates
    - updated API for the web version
    - webapp
- our project proposal

