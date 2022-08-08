# STARBLAST VIEWER

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

> A tool that can augment papers with external information to improve reading experience.
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

## Sections
### <h1> Document viewer with enhanced reading expierence </h1>


## Short Description 
 This project is web based application use for increasing user expirence while reading any new paper articles. 
 comprises of many features as mention below 

- <b>short summary </b>
   - In this using machine learning based technique and text analysis.
- <b> highlighting keywords </b>
   - Trained model library is used for  extracting important keywords and also highlight them in pdf with specific color. 
- <b> discusiion forum </b>
   - Also provide the discussion forum for user to dicuss among the topics for any articles related.


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

### Contributing
Links Contributing 
- python text analysis (https://www.analyticsvidhya.com/blog/2018/02/the-different-methods-deal-text-data-predictive-python/)


## Documentation

### Scope
>Phase 1 document 1.2  

The goal of our project is to create a machine-learning assisted web application that improves news & research article reading for usersby providing them features which involve document editing, commenting and sharing with in a private space,along with automatic summarization of text,thereby augmenting a shift from a passive reading process to an interactive and collaborative experience.

### UI
- Index page  
- Log in / Sign up window  
- Readable articles list  
- Article reading interface  
- Auto-generated summation  
- Comment / Discussion section  

### Features
>Phase 1 document 2.2  

- Allow users to register and login their account.  
- Allow users to search papers discussion if they have been uploaded on the website in its user profile section.  
- Allow users to upload files locally and view them on the website.  
- Allow users to obtain a summary of the paper through machine learning (ML) and text analysis.  
- Automatically highlight important terms in the paper through ML and also allow the user to interactively highlight terms.  
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
  > IN this file we input the URL link and generate the pdf as ouput so that pdf can be use for further feature as summary and highlights.
