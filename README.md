# SocioLyze v0.1.0


### Overview

This project uses the Natural Language Toolkit (NLTK) to analyze Twitter stream
data. SocioLyze gets the Twitter stream from a given user via command-line input,
tokenizes the tweets using NLTK's tokenizer, and then plots the most commonly
used words as a cumulative frequency distribution.

SocioLyze is currently in its early stage, but in the future will be much more
robust, allowing for a wide array of user-input options. In the current version,
0.1.0, the tweets are tokenized and plotted, but many of the given tweets are
retweets and other undesirable user data. Additionally, word filtering needs
to be improved when plotting data (current version only removes stopwords).

### Why SocioLyze?

SocioLyze was created with the intention of analyzing the Twitter feeds of news
agencies in order to examine usage of keywords and analyze bias. Although this is
still the primary intention, SocioLyze will, ideally, be a useful analytical tool
for a much broader range of cases than just examining bias in the news.

### Installation and use

Simply clone this repo to install SocioLyze. In a future release, the
requirements.txt will be included to allow for simple installation of dependencies.
Currently, the only dependencies are the NLTK and Tweepy.

In order to get started with SocioLyze, once the repo has been cloned, adjust the
Tweepy API variables in your tweet_miner.py file to the correct ones provided
by your TWitter account. Then, run tweet_miner.py. After this, run tweet_nltk.py
to plot the Twitter data.

Data in tokenized_tweets.txt, twitterstream_results.txt, and python.json will
be subject to change/deletion in each release. They are useful for doing initial
tests with SocioLyze, but will be appended with more data whenever tweet_miner.py
is run. The data in these text and JSON files is NOT static.

### Notes

This project is a small personal project with only myself as a contributor. It
will be updated with new releases when possible, and functionality will be added
slowly. Pull requests and contributions are more than welcome!
