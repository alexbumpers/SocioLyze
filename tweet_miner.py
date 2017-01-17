from tweepy import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy

"""
Find twitter user ID from username using twitter API
GET https://api.twitter.com/1/users/lookup.json?screen_name=somename
"""

# Variables for logging in to Twitter
access_token = "778255209378160640-uKycCizjOeFDfOwkR6jyWmsGKEDHy7p"
access_token_secret = "cMmkrUd28WzjbNIbTZyvwQAa9LGNH8vuwwfg4W7Yktvdg"
consumer_key = "fBj8qnzsLZPKuwuau3hk6nS3M"
consumer_secret = "NcOehUVeh8dRyylQaAIHf38JuQBkcv10HDWu675Xp91Jut7uvg"

# Variables for authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Defines class that takes data from Twitter stream and write to .txt file
# 'a' == appends
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        #print(status.text())
        #print(status.user.screen_name())
        # Write contents of 'data' variable to twitterstream_results.txt
        with open('twitterstream_results.txt','a') as textfile:
            textfile.write(data)
        return True

    def on_error(self, status):
        print(status)
        # Write status message (e.g. error 406) to file on error
        with open('twitterstream_results.txt','a') as textfile:
            textfile.write(status)

if __name__ == '__main__':

    # Handles Twitter authentification & connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # Streams tweets for only tweets from @FoxNews using Twitter user ID number
    stream.filter(follow=input('''Please enter a Twitter user\'s ID number in the format ['1234567'], including the opening and closing brackets and quotes: '''))

    """ Below is the previous stream via Twitter ID without input for reference. """
    # stream.filter(follow=['1367531'])
