import twitter, os

twitter_api = twitter.Api(consumer_key=os.getenv('CONSUMER_KEY'), 
                  consumer_secret=os.getenv('CONSUMER_SECRET'),
                  access_token_key=os.getenv('ACCESS_TOKEN'),
                  access_token_secret=os.getenv('ACCESS_TOKEN_SECRET'))


print(results)
puppy_results = twitter_api.GetSearch(term='puppies', count=1)
