from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import requests
from bs4 import BeautifulSoup
import re

URL = 'https://www.yelp.com/biz/social-brew-cafe-pyrmont'
TOKENIZER = 'nlptown/bert-base-multilingual-uncased-sentiment'
MODEL = 'nlptown/bert-base-multilingual-uncased-sentiment'

class BertSentimentAnalyser:
    def __init__(self, tokenizer=TOKENIZER, model=MODEL, url=URL):
        self.url = url
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer)
        self.model = AutoModelForSequenceClassification.from_pretrained(model)

    # Returns a list of reviews from the website.
    def get_reviews(self):
        print('Getting reviews from {}...'.format(self.url))
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, 'html.parser')
        regex = re.compile('.*comment.*')
        results = soup.find_all('p', {'class':regex})
        reviews = [result.text for result in results]
        print('Found {} reviews.'.format(len(reviews)))
        return reviews

    # Returns a sentiment score between 1 and 5.
    def sentiment_score(self, review):
        tokens = self.tokenizer.encode(review, return_tensors='pt')
        result = self.model(tokens)
        return int(torch.argmax(result.logits))+1
    
    # Returns a dict of sentiment scores for each review.
    # Max token size for the current LLM model is 512, so we only use the first 512 tokens of each review.
    def get_sentiment_scores(self):
        scores = {}
        reviews = self.get_reviews()
        print('Calculating sentiment scores...')
        # Only use the first 5 reviews for demonstration purposes.
        i = 0
        for review in reviews:
            if i < 5:
                score = self.sentiment_score(review[:512])
                scores[review] = score
                i+=1
        return scores
    

if __name__ == '__main__':
    analyser = BertSentimentAnalyser()
    scores = analyser.get_sentiment_scores()
    for review in list(scores.keys()):
        print("Review: %s - Score: %s \n\n" % (review, scores[review]))
