# freuquency= [# of occurrences of the term in all tweets]/[#of occurrences of all terms in all tweets]
import sys
import json 
from collections import Counter


def relative_freq(tweet_text):
    
    return Counter(word for text in tweet_text for word in text)

def main():
    
    tweet_file = sys.argv[1]

    with open(tweet_file, 'r') as f:
      
        for line in f:
            # text->extraction->encoding
            text = json.loads(line, encoding = 'utf-8').get('text', '')
            tweet_text=[text]
            
    freq=relative_freq(tweet_text) 
    sum_f=sum(freq.values())           

    for i in freq:
            sys.stdout.write('{0} {1:f}\n'.format(i,freq[i]/sum_f))

               
                                        
if __name__ == '__main__':
    main()
