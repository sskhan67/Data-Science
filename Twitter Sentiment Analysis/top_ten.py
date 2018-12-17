import sys
import json
from collections import Counter

def top_ten_hashtag(tweet_file):
    with open(tweet_file) as f:
        hashtag=(json.loads(i).get('entities',None) for i in f)
        tw=(j.get('hashtags') for j in hashtag if j)
        texts=(i['text'] for l in tw for i in l)
        return Counter(texts).most_common(10)



    
def main():
    tweet_file=sys.argv[1]
    top_ten_tag=top_ten_hashtag(tweet_file)
    for i in top_ten_tag:
        sys.stdout.write('{0} {1}.0\n'.format(*i))
                
    
if __name__ == '__main__':
	main()
