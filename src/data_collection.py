import tweepy
import json
from config import TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET

# Configurando a API do Twitter
def authenticate():
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
    return tweepy.API(auth)

def collect_tweets(query, count=100):
    api = authenticate()
    tweets = api.search_tweets(q=query, count=count, tweet_mode='extended')
    tweet_data = [{'id': tweet.id_str, 'text': tweet.full_text, 'created_at': tweet.created_at} for tweet in tweets]
    with open('tweets.json', 'w') as file:
        json.dump(tweet_data, file)

if __name__ == "__main__":
    collect_tweets("#DataScience", 200)
