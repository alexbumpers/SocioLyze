import nltk
from nltk import FreqDist
from nltk import word_tokenize
import re
import json
from pprint import pprint
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
json_data=[]
with open("python.json", "r") as f:
    for line in f:
        append_data = json_data.append(json.loads(line))
print(json_data[0]['text'])[4]
print(json_data[1]['text'])
print(json_data[2]['text'])
print(json_data[3]['text'])
print(json_data[4]['text'])

#data = json.dumps(json_data)
#data = json.loads(json_data)
#pprint(data)


#finder = ([w for w in tt_text if re.search('^Trump$', w)])
# FreqDist for Twitter stream
#tweet_fdist = FreqDist(finder)
"""print(tweet_fdist)
tweet_cfd = tweet_fdist.plot(50, cumulative=True)
print(tweet_cfd)"""
#json_tweet = open("twitterstream_results.txt").read()

"""import json
parsed_json = json.loads(json_tweet)
print(parsed_json['text'])"""
