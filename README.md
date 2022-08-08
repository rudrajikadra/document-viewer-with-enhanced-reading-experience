# STARBLAST | Document viewer with enhanced reading expierence

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

## Short Description 
A web based application that converts passive reading experience of articles into an active reading experience by
- Generating a Short Summary of the uploaded article
- Automatic pagewise extraction of links embedded in the article
- Automatic highlighting of key sentences and display most-valued keywords backlinked to google search result
- Discusiion forum with voting system
- Allows importing articles either as pdf or directly from URLs 

> Live Version: http://starblast.herokuapp.com/index


## Table of Contents

- [Sections](#sections)
  - [Short Description](#short-description)
  - [Install](#install)
  - [Usage](#usage)
  - [Update](#update)
  - [Contributing](#contributing)
- [Documentation](#documentation)
  - [Scope](#scope) 
  - [UI](#ui)
  - [Features](#features)
  - [Team Managment](#team-management)
  - [Code Brief Description](#Code-brief-description)

## Code Structure
``` bash
- static----------------# Static Files of the website
  - css-----------------# styling
  - fonts---------------# fonts used
  - highlighted_pdf-----# Stores the highlighted pdf documents
  - images--------------# Stores images used in website
  - js------------------# bootstrap and jquery scripts         
  - pdf-----------------# Stores the pdfs uploaded to the website

- templates-------------# HTML pages
  - 404.html------------# 404 page
  - company.html--------# The My Teams | to access all the documents uploaded by the team
  - dashboard.html------# The User's Dashboard | access all the documents uploaded by the suer
  - index.html----------# landing page of website
  - login.html----------# login page
  - pricing.html--------# pricing page
  - service.html--------# our services offered page
  - signup.html---------# signup page
  - viewer.html---------# The main PDF viewer site that the user gets upon clicking on 'view' in dashboard. Displays all features such as Highlighting, Keywords, Discussion Thread
  
- app.py----------------# Main Flask Application Code     
- highlight.py----------# Keyword extraction and content highlighting
- mysqlconn.py----------# mysql configuration file
- pdfToSummary.py-------# Generate summary of pdf file
- pdfToURLS.py----------# Get the embedded URLs of each page ; obtain top keywords and provide random 10
- urlToPDF.py-----------# Extract information from provided URL, convert to PDF
- viewer.sql------------# dumped sql file for importing into database when required
```

### Install 

Ideally runs perfectly on Python 3.9.7 with the dependencies listed in requirements.txt file.

using the pip command to install all of the requirements packages  for application 
``` bash
$ pip install -r requirements.txt
```
Also need to install the mySQL database and optionally Apache server ( to see database in browser ).


### Usage 

To run application ,first step need to done is to run app.py file in python CLI .
``` bash 
python app.py
```
This will give you the localhost url for the website start page 
After this user can use the website smoothly.


### Update
In this versioning of our base application take place and also keep on updating our main key features. 

### References to key external packages used
- Multirake Python Package [(https://pypi.org/project/multi-rake/)] : For Extracting Keywords
- Trafilatura [https://trafilatura.readthedocs.io/en/latest/usage-python.html ] : For extracting test from URLs
- Fpdf [ https://pyfpdf.readthedocs.io/en/latest/]: For converting text to PDF

## Project Documentation
### Contributors
``` bash 
- Rudra Jikandra : Front End, Back End, Integration                         (26.66% Contribution)
- Shridhar Prabhuraman : Back End, Integration, Live Configuration          (26.66% Contribution)
- Vibhu Sharma : Summary Generation, Keyword Extraction and all ML features (26.66% Contribution)
- Yui Chan : Highlighting Feature, Documentation                            (20.00% Contribution)
```

### Scope
The goal of our project is to create a machine-learning assisted web application that improves news & research article reading for users by providing them features which involve document editing, commenting and sharing with in a private space,along with automatic summarization of text,thereby augmenting a shift from a passive reading process to an interactive and collaborative experience.  

### Features
- Allow users to register and login their account.  
- Allow users to upload files locally and view them on the website.  
- Allow users to obtain a summary of the paper through Machine learning and text analysis.  
- Automatically highlight important terms in the paper through ML.  
- Allow users to communicate and participate in discussions around the papers via a system where the healthiest post obtains the highest points. (StackOverflow like). Those discussions are visible to all users.  
- Providing explanations and hyperlinks when cursor hovering over highlighted terms and  mentions.

### Team Management
 - For team managment and work distribution we use Agile frame work and Teams to conduct most of team meeting (fornightly).
 - For keep on updating our key feature we use google docs and teams file sharing.
 - Use Github for repo to keep control of version controlling and share code among team mates.

### Code Brief Description
In this brief discription of each code files has been discuss
- app.py
  > This is main flask file of our application, from which our application run on web server. 
- pdfToSummary.py
  > In this code get short summary from the whole text file pdf by using  NLp(Natural Language procesing) and machine learning.
- highlight.py
  > In this code mainly highlighting the keywords among the whole pdf by using Text analysis.
- mysqlconn.py
  > this file is key to connect application to the sql server.
- pdftoURLS.py
  > By using this file we ellobrate the url among the pdf context and give url as output for user further information.
- urlToPDF.py
  > In this file we input the URL link and generate the pdf as ouput so that pdf can be use for further feature as summary and highlights.
