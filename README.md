# BERT_Projects_NLP
Projects  based on Google's BERT Language model 

### 1) Extracting the summary of a blog post automatically using BERT Langauge model.
BERT is a language model trained on huge amount of NLP datasets. This can understand and reproduce human like text.
In this project we use BERT API from Hugging Face library to give us the summary of an article, blogpost or a research paper.

#### How to use this (at the moment):
* Clone/Download the BERT summerizer ipynb file/py file locally. 
* Recommended to use a system having GPU CUDA support / Colab env.
* Replace the URL and html tags you would like to scrap the content for.
* Run the file. The summary output gets saved to a file locally.


* TODO's
- [ ] Setup this to run in a conda env.
- [ ] Modify the code to pass URL, html tags for scraping, output file as arguments.
- [ ] Add code to make this a chrome extension app.


This is highly hepful when one wants to read lot of research papers or blogs.


### 2) Analyzing the review's and extracting the sentiment of those reviews on a scale of 1-5.
Here we scrap a webiste (say UberEats, yelp, Amazon) for the reviews. Pass these reviews to a language model like BERT to analyse the text/reviews and give us a sentiment score of 1-5. BERT api is taken from Hugging face library.

#### How to use this (at the moment):
* Clone/Download the BERT Sentiment Analyser ipynb file/py file locally. 
* Recommended to use a system having GPU CUDA support / Colab env.
* Replace the website URL and html tags you would like to scrap the content for.
* Run the file. The sentiment for each review in the provided webiste is stored in a dataframe gets displayed in the console or saved.

* TODO's
- [ ] Setup this to run in a conda env.
- [ ] Modify the code to pass URL, html tags for scraping, output file as arguments.
- [ ] Add add recursive scraping to scrap all the available reviews (say for a particular restaurant, product etc).
- [ ] Add wordcloud for better visualization and overall view of the reviews.

This is highly useful to get an instant view of how a restarant,company, product is performing.
