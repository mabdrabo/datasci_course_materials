import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    for line in tweet_file:
        line = json.loads(line)
        if 'delete' not in line:  # excluding delete messages
            if line['lang'] == 'en':  # excluding non-english tweets
                text = line['text']
                score = 0
                for term in text.split():
                    if term in scores:
                        score = score + scores[term]
                print score

if __name__ == '__main__':
    main()
