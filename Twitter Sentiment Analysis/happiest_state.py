# happiest stae= score of the particular state/no of state from twitter data  -->
# work flow: read AFINN-111.txt file and tweet file-> state calculation-> state score/no. of state

import sys
import json
from collections import defaultdict



def t_score(tweet, scores):
    return sum(scores.get(word, 0) for word in tweet.split())


def parse(tweet):
    try:
        country = tweet['place']['country_code']
        state = tweet['place']['full_name'].split(", ")[1]
        text = tweet['text']
        return country, state, text
    except (KeyError, TypeError, IndexError):
        return None


def main():
    #file input
        sent_file = sys.argv[1]
        tweet_file=sys.argv[2]

        # read afinn-111.txt
        with open(sent_file) as f:
            sent_scores={line.split('\t')[0]: int(line.split('\t')[1]) for line in f}
            
        t_number, scores, happiness = [defaultdict(float) for _ in range(3)]
        # read tweet file and do calculation
        with open(tweet_file) as f:
            tweets = (json.loads(i) for i in f)# load json file
            tweets_parsed = (parse(j) for j in tweets if parse(j)) # parsed tweet data
            # state score calculation
            state_s = ((state, t_score(text, sent_scores)) for country, state, text in tweets_parsed if len(state) == 2 and country == 'US')

            for state, score in state_s:
                t_number[state] += 1
                scores[state] += score
                happiness[state] = scores[state] / t_number[state] # happiest state
            print (max(happiness, key=happiness.get))
                                    


if __name__ == '__main__':
    main()
