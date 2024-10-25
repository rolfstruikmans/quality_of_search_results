# About Search Engines, and how to find relevant answers in High Dimensional Swiss Cheese
LLMs always provide an answer, but the answer is not always correct. I wanted to develop something that tells you how well you can trust the answer. This is the Final Project of my WBS Data Science Bootcamp showcasing how Search Engines and LLMs can be enhanced with a relevance measure that indicates the relevance of search results with respect to the question you asked.

<div style="display: flex;">
  <img src="images/high_dimensional_cheese.jpg" style="height: 180px;">
  <img src="images/P1120589.JPG" style="height: 180px;"> 
  <img src="images/frankenstein_1984.jpg" style="height: 180px;">
  <img src="images/robotsalut.png" style="height: 180px;">
</div>

----
## Project
LLMs always provide an answer, but the answer is not always correct. I wanted to develop something that tells you how well you can trust the answer. This is the Final Project of my WBS Data Science Bootcamp showcasing how Search Engines and LLMs can be enhanced with a relevance measure that indicates the relevance of search results with respect to the question you asked.

The goal of this project was to develop and showcase a relevance measure for Search Engines and LLMs during a limited time of 2.5 weeks with a clearly defined deliverable using agile methods.  
 
The deliverable is the demonstration of the relevance measure, applied to theoretical, self generated data, i.e. homogeneous data points vs. in-homogeneous data points and to practical data, two search engines, each of them fed with a single book as their corpus. The relevance measure provides a number for search results or chatbot-answers between 0 and 1. A relevance number of 0 means that the search result is completely irrelevant, a relevance number of 1 means that the search result is completely relevant. 

The relevance measure is demonstrated for the **theoretical data** by representing a question as a data point in both a corpus of **homogeneous data points** and a corpus of **in-homogeneous data points**, determining the relevance number in both cases and comparing them for both cases. 

The relevance measure is demonstrated for the **practical data** by asking questions to two different search engines, each of them fed with a different book as its data. One search engine is fed with the book **Frankenstein** by Mary Shelley and the other search engine is fed with the book **1984** by George Orwell. Then five questions are asked to both search engines, two of which apply to the book Frankenstein, two other questions apply to the book 1984, and the final question has nothing to do with either of the two books. The resulting relevance numbers are listed in a table shown on page [xx] in [presentation](/DS-029 Final Project - Presentation.pdf).  

## Recommender Implementation

## Key Learning

## Languages, tools and libraries
- numpy
- pandas
- langchain
- LLMs
- Embeddings
- HuggingFace
- FAISS
- similarity search

## Schedule

## Data Sources
The books **Frankenstein** and **1984** are downloaded from
- https://www.gutenberg.org/


