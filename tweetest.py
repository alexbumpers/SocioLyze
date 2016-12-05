import tweepy


access_token = "778255209378160640-uKycCizjOeFDfOwkR6jyWmsGKEDHy7p"
access_token_secret = "cMmkrUd28WzjbNIbTZyvwQAa9LGNH8vuwwfg4W7Yktvdg"
consumer_key = "fBj8qnzsLZPKuwuau3hk6nS3M"
consumer_secret = "NcOehUVeh8dRyylQaAIHf38JuQBkcv10HDWu675Xp91Jut7uvg"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

stuff = api.user_timeline(screen_name = 'FoxNews', count = 100, include_rts = True)

print(stuff)
