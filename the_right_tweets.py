import twitter, os, nltk

twitter_api = twitter.Api(consumer_key=os.getenv('CONSUMER_KEY'), 
                  consumer_secret=os.getenv('CONSUMER_SECRET'),
                  access_token_key=os.getenv('ACCESS_TOKEN'),
                  access_token_secret=os.getenv('ACCESS_TOKEN_SECRET'))

puppy_tweets = twitter_api.GetSearch(term='puppies')

def get_tweet_sentiment(self, tweet): 
    return TextBlob(tweet.text) 
    
#print(puppy_tweet.text)
