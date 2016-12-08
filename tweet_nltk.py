import nltk
from nltk import FreqDist
from nltk import word_tokenize
import re
import json
from pprint import pprint

class Tweet_Print():
    """Return and print contents of the 'text' key within tweets from JSON data.
    """
    def tweet_print():
        json_data=[]    # Initialize this list so that it may be appended below.
        with open("python.json", "r") as f:
            for line in f:
                append_data = json_data.append(json.loads(line))
            print(json_data[1]['text'])
            print(json_data[2]['text'])
            print(json_data[3]['text'])
            print(json_data[4]['text'])
        """ Creates a freqdist for first tweet. Temporary. Next commit should
        place this capability into the Word_Frequencies class below and
        plot data from all of the tweets.
        """
        tweets_tokenize = nltk.word_tokenize((json_data[1]['text']))
        tweets_nltk = nltk.Text(tweets_tokenize)
        #word_finder = ([w for w in tweets_nltk if re.search('^Trump$', w)])
        tweets_fdist = FreqDist(tweets_nltk)
        tweets_cfd = tweets_fdist.plot(10, cumulative=True)
    print(tweet_print())

#class Word_Frequencies(Tweet_Print):
    #"""Plot/visualize data obtained from Tweet_Print class above."""
    #def tweet_fdist():
        #"""Creates a frequency distribution of most common words within tweets
        #that have been parsed from JSON data above. This is done using the
        #NLTK library. Tweets are tokenized, converted to a format
        #readable by NLTK, and finally plotted into a frequency distribution.
        #"""
        #tweets_tokenize = nltk.word_tokenize(Tweet_Print.tweet_print())
        #tweets_nltk = nltk.Text(tweets_tokenize)
        #word_finder = ([w for w in tt_text if re.search('^Trump$', w)])
        #tweets_fdist = FreqDist(word_finder)
        #tweets_cfd = tweets_fdist.plot(10, cumulative=True)
    #print(tweet_fdist())




# Opens text file with Twitter stream data as JSON file
#def process_or_store(tweet):
    #print(json.dumps(tweet))
# Opens text file with Twitter stream data
#tweet_text = open("twitterstream_results.txt").read()
# Tokenizes tweet_text
#tt_tokenize = nltk.word_tokenize(tweet_text)
# Converts into text that we can analyze with NLTK
#tt_text = nltk.Text(tt_tokenize)
#

#finder = ([w for w in tt_text if re.search('^Trump$', w)])
# FreqDist for Twitter stream
#tweet_fdist = FreqDist(finder)
"""print(tweet_fdist)
tweet_cfd = tweet_fdist.plot(10, cumulative=True)
print(tweet_cfd)"""
#json_tweet = open("twitterstream_results.txt").read()

"""import json
parsed_json = json.loads(json_tweet)
print(parsed_json['text'])"""
