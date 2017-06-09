import os
import tweepy
class Process:
    #if it is not reply, quote or retweeted tweet, open file and add and retweet
    #every month we give the bot a new filename to make and adjust the since_id in the main.
    #this is a way to manage the files without making one large file with outdated tweet IDs
    def addTweet(self, tweet, api):
        try:
            tweetID = tweet.id_str
            original_Tweet = tweet
      
            retweet = getattr(tweet, "retweeted_status", None)  #checks if it is a retweet, returns None otherwise
            reply = getattr(tweet, "in_reply_to_status_id", None) #checks if it is a reply, returns None otherwise
            quote = getattr(tweet, "quote_status_id", None) #checks if it is a quote, returns None otherwise
                
            if(retweet is not None):
                print("is a retweet")
                tweetID = tweet.retweeted_status.id_str
                original_Tweet = api.get_status(int(tweetID))
                print(tweetID)
                print("retweet")
            #original_Tweet.retweet()
           
                
            elif (reply is not None):
                print("is a reply")
                tweetID = tweet.in_reply_to_status_id_str
                original_Tweet = api.get_status(int(tweetID))
                print(tweetID)
                print("retweet")
            #original_Tweet.retweet()
            #api.retweet(int(tweetID))
 
                
            elif(quote is not None):
                print("is a quote")
                tweetID = tweet.quoted_status_id_str
                print("quote")
                original_Tweet = api.get_status(int(tweetID))
            #original_Tweet.retweet()
            #tweet.retweet(int(tweetID))
       
            else:
                print("just a regular tweet")
                print(tweetID)

            file = open("reTweetsMay.txt", "a+")
            file.seek(0) #takes the cursor to the beginning of the file for searching purposes
            lines = file.readlines()
            print(lines)
            if (os.stat("reTweetsMay.txt").st_size == 0):
                print("file is empty\n")
              
            else:
                print("here")
                for storedID in lines:
                    print(storedID)
                    storedID = storedID.strip("\n")
                    if (tweetID == storedID):
                        print("already retweeted\n")
                        file.close()
                        return
                
            original_Tweet.retweet()  
            file.write(tweetID+"\n")
            file.close()
        except Exception as e:
            return
