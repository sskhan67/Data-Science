import sys
import json 



def main():
    
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    scores = {}
    with open(sent_file, 'r') as f:
        for line in f:
            # The file is tab-delimited.
            term, score  = line.split("\t")  
            scores[term] = int(score)
            
  

    with open(tweet_file, 'r') as f:
        for line in f:
            # text->extraction->encoding 
            tweet_text = json.loads(line, encoding = 'utf-8').get('text', '')
            # sentiment calculation
            t=0
            for word in tweet_text.split(" "):
                t=t+scores.get(word,0)
                
            sys.stdout.write('{0:d}\n'.format(t))

    
if __name__ == '__main__':
    main()
