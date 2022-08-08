from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
import sys
from PyPDF2 import PdfReader
import re


# This function takes the entire text and preprocesses it with splitting into sentences.
def read_article(content):
    article = content.strip().replace("  ", " ").split(".")
    
    while("" in article):
        article.remove("")

    while(" " in article):
        article.remove(" ")

    newArticle = []
    for eachSent in article:
        if (len(eachSent) > 40):
            newArticle.append(eachSent)

    sen = []
    for sentence in newArticle:
        sen.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    sen.pop()
    
    return sen


# This function will identify the correlation between two sentences and finds the cosine similarity between them.
def sentence_similarity(sent1, sent2, stopwords=None):
    
    if stopwords is None:
        stopwords = []
 
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
 
    all_words = list(set(sent1 + sent2))
 
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
 
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1
 
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1
 
    return 1 - cosine_distance(vector1, vector2)


# Applying cosin similarity over all the data to collect most important words for each sentence
def build_similarity_matrix(sentences, stop_words):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
 
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2: 
                continue 
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

    return similarity_matrix


# This will then generate the entire summary using the key sentences found using the function build_similarity_matrix
def generate_summary(fileContent,f=8):
    
    stop_words = stopwords.words('english')
    summarize_text = []
    sentences = read_article(fileContent)


    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)

    graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank(graph)
    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)

    f = len(ranked_sentence)/5
    if len(ranked_sentence) >= int(f):
        for i in range(int(f)):
            summarize_text.append(" ".join(ranked_sentence[i][1]))
    else:
        for eachRankedSentence in ranked_sentence:
            summarize_text.append(" ".join(eachRankedSentence[1]))

    finalSummary = ". ".join(summarize_text)

    return str(finalSummary)


# This is the main file call function that will take file name as input and returns the generated text summary
def pdfToSummary(name):
    try:
        doc = "static//pdf//" + str(name)
        # print(doc)

        reader = PdfReader(doc)

        text = ""
        for page in reader.pages:
            text += page.extract_text().replace("\n", " ") + " "

        #with open("intermediateFile.txt", 'w') as f:
         #    f.write(text)

        finalSumm = generate_summary(text, 8)
    except:
        finalSumm = ""
        
    return finalSumm


