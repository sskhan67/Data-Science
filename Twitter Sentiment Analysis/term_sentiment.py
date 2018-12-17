# term sentiment calculation work flow: load two txt file-> find not in affinfile : set score zero and count-> calculate score 
import sys
import json 


def main():
    
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    scores = {}
    with open(sent_file, 'r') as f:
        for line in f:
            # tab-delimited tab
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
                
            for word in tweet_text.split(" "):
                    if word not in scores:
                        non_afinn_pairs={word:t}
                    for i,j in non_afinn_pairs.items():
                        sys.stdout.write('{0} {1:d}\n'.format(i,j))

                                         
if __name__ == '__main__':
    main()
