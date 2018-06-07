import tweepy
import csv
import time

from keys import keys

screen_name = keys['screen_name']
consumer_key = keys['consumer_key']
consumer_secret = keys['consumer_secret']
access_token = keys['access_token']
access_token_secret = keys['access_token_secret']

username = input("Give me a Twitter handle: ")
user = username

file = open("followerslist.txt", "w", encoding = "utf-8")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


users = tweepy.Cursor(api.friends, screen_name = username).items()

while True:
    try:
        user = next(users)
    except tweepy.TweepError:
        time.sleep(60*15)
        user = next(users)
    except StopIteration:
        break
    print ("@" + user.screen_name)
    file.write("@" + user.screen_name + "\n")
    
file.close()


print("\n")


