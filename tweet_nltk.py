import nltk
from nltk import FreqDist
from nltk import word_tokenize
import re
# Opens text file with Twitter stream data as JSON file
def process_or_store(tweet):
    print(json.dumps(tweet))
# Opens text file with Twitter stream data
tweet_text = open("twitterstream_results.txt").read()
# Tokenizes tweet_text
tt_tokenize = nltk.word_tokenize(tweet_text)
# Converts into text that we can analyze with NLTK
tt_text = nltk.Text(tt_tokenize)
#
finder = ([w for w in tt_text if re.search('^text$', w)])
# FreqDist for Twitter stream
tweet_fdist = FreqDist(finder)
print(tweet_fdist)
tweet_cfd = tweet_fdist.plot(50, cumulative=True)
print(tweet_cfd)
#json_tweet = open("twitterstream_results.txt").read()

"""import json
parsed_json = json.loads(json_tweet)
print(parsed_json['text'])"""
