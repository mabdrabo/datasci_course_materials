import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    non_dic_terms = {}  # terms that are not in the dictionary

    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    for line in tweet_file:
        line = json.loads(line)
        if 'lang' in line:  # excluding all but tweet messages
            if line['lang'] == 'en':  # excluding non-english tweets
                text = line['text'].lower()
                score = 0
                for term in text.split():
                    if term in scores:
                        score = score + scores[term]
                    else:
                        non_dic_terms[term] = []
                for term in non_dic_terms.keys():
                    if term in text.split():
                        non_dic_terms[term].append(score)

    for k,v in non_dic_terms.items():
        print k, sum(v)

                    

if __name__ == '__main__':
    main()
