from dotenv.main import load_dotenv
import requests
import os
import pandas as pd
import time
import numpy as np
from requests.api import post
from sqlalchemy import create_engine


def connect_db():
    load_dotenv()
    engine = create_engine(os.getenv('uri'))
    tweets = pd.read_sql_table("tweets_df", engine, index_col=0)
    tweets = tweets.iloc[0]
    return tweets


def post_on_slack(tweets):
    data = {'text':
            f"----New tweet has arrived----\n{tweets['username']}: {tweets['tweet']}\n----The sentiment score of the tweet----\n{tweets['sentiment']}"
            }
    webhook_url = os.getenv('webhook_url_channel_twitter')
    # webhook_url=os.getenv('webhook_url_my_channel')
    requests.post(url=webhook_url, json=data)


check = 1
tweets = connect_db()
post_on_slack(tweets)
loop = True
while(loop):
    tweets = connect_db()
    if (tweets['table_number'] == check):
        post_on_slack(tweets)
        check = check + 1
    else:
        time.sleep(30)
