import tweepy
import csv
import time

from keys import keys

keepgoing = True


screen_name = keys['screen_name']
consumer_key = keys['consumer_key']
consumer_secret = keys['consumer_secret']
access_token = keys['access_token']
access_token_secret = keys['access_token_secret']


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
    
followers = api.followers_ids(screen_name)
friends = api.friends_ids(screen_name)


for f in friends:
    if f not in followers:
        #ask = input("Unfollow {0}?".format(api.get_user(f).screen_name))
        #if ((ask == "N") or (ask == "n")):
        api.destroy_friendship(f)
