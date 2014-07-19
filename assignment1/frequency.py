import sys
import json

def main():
    tweet_file = open(sys.argv[1])
    term_occ = {}  # occurrences of terms in all tweets
    all_occ = 0  # occurrences of all terms in all tweets

    for line in tweet_file:
        # print type(line)
        line = json.loads(line)
        if 'text' in line:  # excluding all but tweet messages
            if line['lang'] == 'en':  # excluding non-english tweets
                text = line['text'].lower().split()
                all_occ = all_occ + len(text)

                for term in text:
                    if term in term_occ:
                        term_occ[term] = term_occ[term] + 1
                    else:
                        term_occ[term] = 1

    for k,v in term_occ.items():
        print k, v/all_occ

                    

if __name__ == '__main__':
    main()
