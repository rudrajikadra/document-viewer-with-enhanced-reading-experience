# Usage python pdfToURLS.py pdfFile.pdf
# It saves a json file with page numbers and their corresponding links

import sys
from PyPDF2 import PdfReader
import re
import json
from multi_rake import Rake
import random


# Find urls from the entire text of each page of the pdf
def Find(string):
    # findall() has been used 
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)      
    return [x[0] for x in url]


# This is the main function call that takes file name as input and generates all the urls and keywords with their google links
def pdfToUrls(doc):
    try:
        reader = PdfReader("static//pdf//" + doc)

        mainDictionary = {}
        pageNumber = 0
        for page in reader.pages:
            pageNumber += 1
            pageContent = str(page.extract_text())
            eachPageKW_dict = {}

            urlList = Find(pageContent)

            for eachURL in urlList:
                pageContent.replace(str(eachURL), " ")
            
            # Rake is used to identify all the keywords and getting top 10 random keywords to generate google search links
            rake = Rake()
            keywords = rake.apply(pageContent)
            updatedKeyWords = [k[0].replace("'", "").replace("\"", "") for k in keywords if k[1] >= 2.0]
            
            if len(updatedKeyWords) != 0:
                topRKeywords = set(random.choices(updatedKeyWords, k=10))
            else:
                topRKeywords = []

            for eachKW in topRKeywords:
                kw_link = "https://www.google.com/search?q=" + '+'.join(eachKW.split(' '))
                eachPageKW_dict[eachKW] = str(kw_link)


            mainDictionary[str(pageNumber)] = {
                "url": urlList,
                "keyWords": eachPageKW_dict
            }
    except:
        mainDictionary = {}


    # Returns a dictionery that has key as page number and value as another dictionery containing url list of that page 
    # and keywords dictionery with their google search links
    return mainDictionary



# pdfToUrls("Coronavirus.pdf")

