import os
import praw
import json
from praw.models import MoreComments
from dotenv import load_dotenv
load_dotenv()


REDDIT_USERNAME = os.environ.get('REDDIT_USERNAME')
CLIENT_ID = os.environ.get('REDDIT_CLIENT_ID')
SECRET_KEY = os.environ.get('REDDIT_SECRET_KEY')


def get_data(keyword):
    reddit = praw.Reddit(user_agent="Comment Extraction (by /" + REDDIT_USERNAME + ")",
                     client_id=CLIENT_ID, client_secret=SECRET_KEY)

    post = []
    print('crawling started...')
    
    for submission in reddit.subreddit('CryptoCurrency').search(keyword, time_filter='week'):
        for top_level_comment in submission.comments:
            if isinstance(top_level_comment, MoreComments):
                continue
            post.append((top_level_comment.body, top_level_comment.created_utc))
            
    # with open('data.json', 'w') as f:
    #     json.dump(post, f)
    print('crawling ended: {0} posts crawled '.format(len(post)))
    return post
    #print(post)

