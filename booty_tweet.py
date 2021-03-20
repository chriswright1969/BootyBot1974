import tweepy
from time import sleep
from credentials import *
import csv
import random
import re
import main

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)

with open('new_bootlegger1974_tweets.csv') as f:
    reader = csv.reader(f)
    for index, row in enumerate(reader):
        if index == 0:
            chosen_row = row[2]
        else:
            r = random.randint(0, index)
            if r == 0:
                chosen_row = row[2]

chosen_row = re.sub(r'@[^\s]+', '', chosen_row, flags=re.MULTILINE)
print (chosen_row)
# api.update_status(chosen_row)

# main.get_all_tweets("bootlegger1974")
#
sleep(3600)


