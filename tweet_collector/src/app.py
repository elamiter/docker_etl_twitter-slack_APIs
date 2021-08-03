import tweepy
import os
import pandas as pd
import logging
import time
from sqlalchemy import create_engine
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from dotenv import load_dotenv


# filters/levels: priority of the log messages

# DEBUG: detailed diagnostic output
# INFO: status monitoring, everything is working as expected
# WARNING: no immediate action required, something happened (eg disk space low)
# ERROR(CRITICAL also high): some exception to solve, software unable to perform some function

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='/log/tweet_collector.log', filemode='w'
)

# load_dotenv() #it's needed while running on local, not in container
counter = 0
while(True):
    auth = tweepy.OAuthHandler(os.getenv('API_KEY'), os.getenv('API_SECRET'))
    auth.set_access_token(os.getenv('access_token'),
                          os.getenv('access_token_secret'))
    api = tweepy.API(auth)
    logging.debug('collect tweets from the twitter api')

    cursor = tweepy.Cursor(
        api.search,
        q='covid',  # -filter:retweets',
        tweet_mode='extended',
        lang='en')

    analyzer = SentimentIntensityAnalyzer()
    logging.debug('sentiment is initiliased')

    date = []
    user = []
    tweet = []
    sentiments = []
    table_number = []
    logging.info("start extracting data ")

    for status in cursor.items(1):
        date.append(status.created_at)
        user.append(status.user.screen_name)
        tweet.append(status.full_text)

        # sentiment analysis
        sent = analyzer.polarity_scores(status.full_text)
        # compound score between -1 and 1
        # positive: score > 0.05
        # negative: score < -0.05
        sentiments.append(sent['compound'])
        table_number.append(counter)

    #print('transform tweets to a pandas dataframe')
    data = {'date': date, 'username': user, 'tweet': tweet,
            'sentiment': sentiments, 'table_number': table_number}
    tweets = pd.DataFrame(data)
    logging.debug('tweets DataFrame created')

    engine = create_engine(os.getenv('uri'))

    tweets.to_sql("tweets_df", engine, if_exists='replace', index=False)

    logging.debug('completed')
    counter = counter + 1
    time.sleep(600)
