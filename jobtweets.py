import re
from dotenv import load_dotenv
import os
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from argparse import ArgumentParser


class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
       
        load_dotenv()
        consumer_key = os.getenv('consumer_key')
        consumer_secret = os.getenv('consumer_secret')
        access_token = os.getenv('access_token')
        access_token_secret = os.getenv('access_token_secret')
 
       
        try:
         
            self.auth = OAuthHandler(consumer_key, consumer_secret)
         
            self.auth.set_access_token(access_token, access_token_secret)
        
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")
 
    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
 
    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        
        analysis = TextBlob(self.clean_tweet(tweet))
       
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'
 
    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
       
        tweets = []
 
        try:
          
            fetched_tweets = self.api.search(q=query, count=count)
 
           
            for tweet in fetched_tweets:
               
                parsed_tweet = {}
 
               
                parsed_tweet['text'] = tweet.text
               
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
 
                if tweet.retweet_count > 0:
                 
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
 
        
            return tweets
 
        except tweepy.TweepError as e:
            print("Error : " + str(e))


def main():
    parser = ArgumentParser(description=__doc__, add_help=False)
    parser.add_argument('--keyword', action='store', help='a keyword to query on')
    query = parser.parse_args()
    api = TwitterClient()
    tweets = api.get_tweets(query=query.keyword, count=500)

    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    if ptweets:
        print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
        print("Positive tweets:\n")
        for tweet in ptweets[:10]:
            print(tweet['text'])
    else:
        print("Positive tweets percentage: 0 %\n")

    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    if ntweets:
        print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
        print("Negative tweets:")
        for tweet in ntweets[:10]:
            print(tweet['text'])
    else:
        print("Negative tweets percentage: 0 %\n")

    if len(ptweets) != len(ntweets):
        print("Neutral tweets percentage: {} % ".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)))
        print("Neutral tweets:\n")
        neutrals = [tweet for tweet in tweets if (tweet not in ptweets) and (tweet not in ntweets)]
        for tweet in neutrals[:10]:
            print(tweet['text'])
    else:
        print("Neutral tweets percentage: 0 %")


if __name__ == "__main__":

    main()
