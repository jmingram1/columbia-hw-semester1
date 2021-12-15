# Fall 2021 Data Homework, Columbia Journalism School 

Hello! This repository contains homework assignments completed for my two data and computing courses in my first semester as an M.S. Data Journalism student at Columbia. The assignments were for **Foundations of Computing**, taught by Jonathan Soma, and **Data & Databases**, taught by Jonathan Thirkield, where I learned querying in SQL, cleaning and analyzing data with pandas, scraping the web and parsing text with regular expressions.

Note: The numbering on the files corresponds to the numbers the assignments were given for each class, but can otherwise be disregarded! 

Here is a guide for navigating this repo:

## API

These assignments answer questions by pulling data from:

* [A Pokemon API](api/3-pokemon.py) (More info: https://pokeapi.co)
* [A weather API](api/4-weather.py) (https://www.weatherapi.com)
* [Last.fm's music API](api/4-last-fm.py) (https://www.last.fm/api/)

## Basic Python

* [Birth Year Script](basic-python/1-birth-year-script.py) takes in the user's birth year and returns a bunch of random facts, such as how many times a whale's heart beat in their lifetime or how many Democratic presidents there have been since they were born.
* [The list and dictionaries assignment](basic-python/2-lists-dictionaries.py) creates and perfoms various functions on small lists and dictionaries. 
* [The parsing json assignment](basic-python/3-parsing-json.py) applies the techniques of working with lists and dictionaries by navigating json data.

## Command Line

* [1-cmd-line](command-line/1-cmd-line.txt) contains commands for navigates the CSV file [OSHA-fatalities-FY2017.csv](command-line/OSHA-fatalities-FY2017.csv) in the terminal.

## Mapping

* This directory contains screenshots of maps created in QGIS as per [these directions](https://gist.github.com/jsoma/0865246bd9223a6b86fe6876efb4c640) using data on powerplants in the U.S. 

## Pandas

These assignments use pandas dataframes to clean and analyze data on:

* [Animals](pandas/5-pandas/animals)
* [Billionaires](pandas/5-pandas/billionaires)
* [Beer brands](pandas/6-pandas/beer)
* [Licensed dogs in NYC](pandas/6-pandas/dogs)
* [A subset of 311 calls](pandas/7-pandas-cleaning/311) subset.csv, the subset of 311 data the notebook works with, was too large for GitHub - but the 311 data can be accessed on [NYC Open Data](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9)
* [Cherry blossoms in Japan](pandas/7-pandas-cleaning/cherry-blossoms)

## Regex

Using regular expressions, these assignments parse texts for:

* [Information on U.S. Senators](regex/4.0-regex-senators-wasteland.ipynb), like their phone numbers or party affiliations, and patterns in T.S. Eliot's "The Waste Land"
* [Five different poems](regex/4.1-regex-functions.ipynb), this time by defining functions to find things such as the shortest line or lines starting with a specific word

## Scraping

* [bs-shakespeare](scraping/3.0-bs-shakespeare.ipynb) uses Beautiful Soup to scrape a website with the first act of Shakespeare's The Tempest.
* [bs-court-movies](scraping/3.1-bs-court-books.ipynb) uses Beautiful Soup to scrape Supreme Court decisions and The Guardian's 2017 Top Nonfiction Books List.
* [9-selenium](scraping/9-selenium) contains notebooks that use Selenium to scrape data on Texas cosmotologist violations and Chicago building permits and inspection records.

## SQL

* Assignments [1.1](sql/1.1-mondial.txt) and [1.3](sql/1.3-mondial.txt) use postgres to run SQL queries on the [Mondial database](https://www.dbis.informatik.uni-goettingen.de/Mondial/). The queries were run in the terminal, then copied with the resulting tables into text files. (1.2 was an unrelated assignment and not included.)
* Assignment [2.0](sql/2.0-un-jupyter.ipynb) uses postgres and SQL to run queries on data from the United Nations on energy use, this time in a jupyter notebook rather than in the terminal. 
