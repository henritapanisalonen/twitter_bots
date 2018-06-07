import tweepy
import csv
import time
from tweepy.parsers import RawParser

from keys import keys

keepgoing = True

screen_name = keys['screen_name']
consumer_key = keys['consumer_key']
consumer_secret = keys['consumer_secret']
access_token = keys['access_token']
access_token_secret = keys['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

rawParser = RawParser()

api = tweepy.API(auth_handler = auth, parser = rawParser)

with open("followerslist.txt") as file:
        for line in file:
                user = line.strip()
                api.create_friendship(user)
