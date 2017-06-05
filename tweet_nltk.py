import nltk
from nltk import FreqDist
from nltk import word_tokenize
from nltk.corpus import stopwords
import re
import json

class Tweet_Print():
    """ This file should take in Twitter stream data from python.json, then
    manipulate it using NLTK. Current version tokenizes tweets, prints
    frequency distribution (with exclusion of stopwords currently in testing),
    and plots it as a cumulative frequency distribution (in testing).
    """
    def tweet_print(tweet_data):
        # 'tokenized_tweets.txt' below, for example
        tt_txtfile = tweet_data
        # Initialize this list so that it may be appended below
        json_data=[]
        with open('python.json', 'r') as f:
            # Allows for JSON manipulation using Python
            for line in f:
                append_data = json_data.append(json.loads(line))
                for item in json_data:
                    tweets = item['text']
                    # Open tokenized_tweets.txt
                    with open(tt_txtfile, 'a') as new:
                        # Tokenize tweets
                        tokenized_tweets = nltk.word_tokenize(tweets)
                        print(tokenized_tweets)
                        # 30-34 PSEUDO. Remove unnecessary items from tweets
                        punctuation = ['!', '.', ',', '@', '&', '(', ')']
                        for item in tokenized_tweets:
                            if item not in punctuation:
                                item.remove
                        # Write tweets to file, each on a new line
                        write_tweets = new.write(str(tokenized_tweets) + "\n")


                        print(write_tweets)
        # Converts tweets to format that may be manipulated by NLTK
        tweets_nltk = nltk.Text(tokenized_tweets)
        # Creates a frequency distribution of tweets_nltk
        tweets_fdist = FreqDist(tweets_nltk)
        # Ignores samples that consist of only stopwords or punctuation (in testing)
        stopwords = nltk.corpus.stopwords.words('english')
        punctuation = ['!', '.', ',', '@', '&', '(', ')']
        print([sample for sample in tokenized_tweets if sample not in stopwords or punctuation])
        # Plots a cumulative frequency distribution of words in tweets (in testing)
        tweets_cfd = tweets_fdist.plot(10, cumulative=True)
    tweet_print('tokenized_tweets.txt')
