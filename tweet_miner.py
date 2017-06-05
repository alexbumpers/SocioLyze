from tweepy import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from keys import TwitterKeys
import tweepy

""" Find twitter user ID from username using twitter API
GET https://api.twitter.com/1/users/lookup.json?screen_name=somename
"""

""" This file should be used to stream Twitter JSON data from Twitter into text
files for further manipulation by the tweet_nltk.py file. Currently, it allows
for the user to input the Twitter ID number in the terminal in order to choose
what user's tweets will be streamed.
"""


# Variables for logging in to Twitter
def keys(access_token, access_token_secret, consumer_key, consumer_secret):
    access_token = TwitterKeys.access_token
    access_token_secret = TwitterKeys.access_token_secret
    consumer_key = TwitterKeys.consumer_key
    consumer_secret = TwitterKeys.consumer_secret
    return keys(access_token, access_token_secret, consumer_key, consumer_secret)

# Variables for authorization
auth = tweepy.OAuthHandler(TwitterKeys.consumer_key, TwitterKeys.consumer_secret)
auth.set_access_token(TwitterKeys.access_token, TwitterKeys.access_token_secret)
api = tweepy.API(auth)

# Defines class that takes JSON data from Twitter stream and write to .txt file
class StdOutListener(StreamListener):

    # Twitter stream function: sends streamed tweets to .txt file
    def on_data(self, data):
        print(data)
        # Lines 34-35 unused, kept for future reference
        # print(status.text())
        # print(status.user.screen_name())
        # Write contents of 'data' variable to twitterstream_results.txt
        with open('twitterstream_results.txt','a') as textfile:
            textfile.write(data)
        return True

    # Error handler for the Twitter stream
    def on_error(self, status):
        print(status)
        # Write status message (e.g. error 406) to file on error
        with open('twitterstream_results.txt','a') as textfile:
            textfile.write(status)

if __name__ == '__main__':

    # Handles Twitter authentification & connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(TwitterKeys.consumer_key, TwitterKeys.consumer_secret)
    auth.set_access_token(TwitterKeys.access_token, TwitterKeys.access_token_secret)
    stream = Stream(auth, l)

    # Streams tweets using Twitter ID number via input from user in the command-line
    stream.filter(follow=input('''Please enter a Twitter user\'s ID number in the format ['1234567'], including the opening and closing brackets and quotes: '''))

    # Below is the previous stream via Twitter ID without input for reference:
    # stream.filter(follow=['1367531'])
