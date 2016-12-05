from tweepy import Stream
from tweepy.streaming import StreamListener
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
class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("&quot;Error on_data: %s&quot" % str(e))

    def on_error(self, status):
        print(status)

twitter_stream = Stream(auth, MyListener())
#twitter_stream.filter(track=['#python'])
twitter_stream.filter(follow=['1367531'])
