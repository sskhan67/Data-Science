# Twitter data collection for a specific topics "Trump". Based on "Trump" topics, tweeter sentiment will be collected.

import tweepy
from tweepy import OAuthHandler
import json
import datetime as dt
import time
import os
import sys

# load api using tweeter app data
def load_api():

    consumer_key = 'dYYwg6b1WYlPObGiYsERFjt9r'
    consumer_secret = '682r5dZP3GmRni4Z1k0MZPPGtCCW8hn2pfY6OIVWrdtyoiG3gO'
    access_token = '1036770400124919808-lVkZZ4ZtKftVXfA0aLpZHWttymfoLk'
    access_secret = '5GfOFuzj6TF7sq1sHdGT75G5T6S3aizakkhA3Vq7wh43I'
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    # load the twitter API via tweepy
    return tweepy.API(auth)

   # tweet search module 
def tweet_search(api, query, max_tweets,geocode):
    
    searched_tweets = []
    while len(searched_tweets) < max_tweets:
        remaining_tweets = max_tweets - len(searched_tweets)
        try:
            new_tweets = api.search(q=query, count=remaining_tweets, geocode=geocode)
            print('found',len(new_tweets),'tweets')
            if not new_tweets:
                print('no tweets found')
                break
            searched_tweets.extend(new_tweets)
            
        except tweepy.TweepError:
            print('exception raised, waiting 1 minutes')
            print('(until:', dt.datetime.now()+dt.timedelta(minutes=1), ')')
            break # stop the loop
    return searched_tweets


def get_tweet_id(api, date='', days_ago=1, query='a'):
    

    if date:
        # return an ID from the start of the given day
        td = date + dt.timedelta(days=1)
        tweet_date = '{0}-{1:0>2}-{2:0>2}'.format(td.year, td.month, td.day)
        tweet = api.search(q=query, count=1, until=tweet_date)
    else:
        # return an ID from __ days ago
        td = dt.datetime.now() - dt.timedelta(days=days_ago)
        tweet_date = '{0}-{1:0>2}-{2:0>2}'.format(td.year, td.month, td.day)
        # get list of up to 10 tweets
        tweet = api.search(q=query, count=10, until=tweet_date)
        #print('search limit (start/stop):',tweet[0].created_at)
        # return the id of the first tweet in the list
        return tweet[0].id


def write_tweets(tweets, filename):

    with open(filename, 'a') as f:
        for tweet in tweets:
            json.dump(tweet._json, f)
            f.write('\n')


def main():
   
    search_phrases = ['Trump']
    time_limit = 1.5                           # limit in hours
    max_tweets = 500                           # number of tweets per search 
    min_days_old, max_days_old = 1, 30          # search limits e.g., from 7 to 8
    USA = '39.8,-95.583068847656,2500km'       # this geocode includes nearly all American states
                                            
    # creating a new file for each
    for search_phrase in search_phrases:

        #print('Search phrase =', search_phrase)

        name = search_phrase.split()[0]
        json_file_root = name
        os.path.dirname(json_file_root)
        read_IDs = False
        
        # open a file in which to store the tweets
        if max_days_old - min_days_old == 1:
            d = dt.datetime.now() - dt.timedelta(days=min_days_old)
            day = '{0}-{1:0>2}-{2:0>2}'.format(d.year, d.month, d.day)
        else:
            d1 = dt.datetime.now() - dt.timedelta(days=max_days_old-1)
            d2 = dt.datetime.now() - dt.timedelta(days=min_days_old)
            day = '{0}-{1:0>2}-{2:0>2}_to_{3}-{4:0>2}-{5:0>2}'.format(
                  d1.year, d1.month, d1.day, d2.year, d2.month, d2.day)
        json_file = json_file_root +'.txt' # txt file creation
        if os.path.isfile(json_file):
            #print('Appending tweets to file named: ',json_file)
            read_IDs = True
        
        # load the twitter API
        api = load_api()
        
        # set the 'starting point' ID for tweet collection
        if read_IDs:
            # open the json file and get the latest tweet ID
            with open(json_file, 'r') as f:
                lines = f.readlines()
                max_id = json.loads(lines[-1])['id']
        
        
        #tweet collection
        start = dt.datetime.now()
        end = start + dt.timedelta(hours=time_limit)
        count, exitcount = 0, 0
        while dt.datetime.now() < end:
            count += 1
            #print('count =',count)
            # collect tweets and update max_id
            tweets= tweet_search(api, search_phrase, max_tweets,geocode=USA)
            # write tweets to file in JSON format
            if tweets:
                write_tweets(tweets, json_file)
                exitcount = 0
            else:
                exitcount += 1
                if exitcount == 3:
                    if search_phrase == search_phrases[-1]:
                        sys.exit('exiting')
                    else:
                        print('breaking')
                        break


if __name__ == "__main__":
    main()
