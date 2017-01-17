
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import nltk
from nltk import FreqDist
from nltk import word_tokenize
from nltk.corpus import stopwords
import re
import json
from bs4 import BeautifulSoup

class Tweet_Print():
    """Return and print contents of the 'text' key within tweets from JSON data.
    """
    def tweet_print(tweet_data):
        tt_txtfile = tweet_data  # 'tokenized_tweets.txt', for example
        json_data=[]  # Initialize this list so that it may be appended below
        with open('python.json', 'r') as f:
            for line in f:
                append_data = json_data.append(json.loads(line))
                for item in json_data:
                    tweets = item['text']
                    #print(tweets)  # Print tweets to terminal
                    with open(tt_txtfile, 'a') as new:  # Open tokenized_tweets.txt
                        tokenized_tweets = nltk.word_tokenize(tweets)
                        print(tokenized_tweets)
                        write_tweets = new.write(str(tokenized_tweets) + "\n")
                        print(write_tweets)  # Write tweets + \n to file
        tweets_nltk = nltk.Text(tokenized_tweets)
        tweets_fdist = FreqDist(tweets_nltk)
        # Ignores samples that consist of only stopwords or punctuation (not working)
        stopwords = nltk.corpus.stopwords.words('english')
        punctuation = ['!', '.', ',', '@', '&', '(', ')']
        print([sample for sample in tokenized_tweets if sample not in stopwords or punctuation])

        #print(text_fdist)
        tweets_cfd = tweets_fdist.plot(10, cumulative=True)
    tweet_print('tokenized_tweets.txt')
