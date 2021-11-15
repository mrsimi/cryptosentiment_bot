import os
import tweepy
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get('tw_ApiKey')
SECRET_KEY = os.environ.get('tw_SecretKey')
ACCESS_TOKEN = os.environ.get('tw_accessToken')
SECRET_TOKEN = os.environ.get('tw_accessTokenSecret')

def get_tweets(keyword):
    auth = tweepy.OAuthHandler(API_KEY, SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, SECRET_TOKEN)

    api = tweepy.API(auth)
    # for tweet in tweepy.Cursor(api.search_tweets, q=keyword).items(10):
    #     print(tweet)
    print(api.search_tweets(q='keyword', count='10'))
    