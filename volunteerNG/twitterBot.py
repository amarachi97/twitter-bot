import tweepy
import time
from time import sleep
from tweetProcesses import Process

#bot
consumer_key = ''
consumer_secret = ''
access_token =''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth.secure = True
api = tweepy.API(auth)
myBot = api.get_user(screen_name = '@VolunteerNIG')
process = Process()
#mess = api.send_direct_message(screen_name = '@amarachi_xx', text = "its ami's bot")
#q= 'volunteer%20ibadan%20OR%20lagos%20OR%20looking%20OR%20volunteering%20OR%20volunteers'

for tweet in tweepy.Cursor(api.search,q= 'volunteer%20ibadan%20OR%20lagos%20OR%20abuja' ,lang ='en',since = '2017-06-01' ).items():
    try:
        print("Location: " + tweet.user.location)
        print("Tweet: " + tweet.text)
        #print(tweet)
        print(tweet.created_at)
        tweetID = int(tweet.id)
        if(tweet.user.id == myBot.id): #so you don't retweet yourself
            continue
        process.addTweet(tweet,api)

        print()
        #break
        #sleep(18000) #every 5 hours
    except Exception as e:
        print('an error')
        #sleep (3600)
        continue
