import sys
import json
import operator

def main():
    tweet_file = open(sys.argv[1])
    hash_occ = {}  # occurrences of hashtags

    for line in tweet_file:
        line = json.loads(line)
        if 'lang' in line:  # excluding all but tweet messages
            if line['lang'] == 'en':  # excluding non-english tweets
                text = line['text'].lower().split()
                for h in line['entities']['hashtags']:
                    h = h['text']
                    if h in hash_occ:
                        hash_occ[h] = hash_occ[h] + 1
                    else:
                       hash_occ[h] = 1

    sorted_x = sorted(hash_occ.iteritems(), key=operator.itemgetter(1), reverse=True)
    top_ten = sorted_x[:10]

    for top in top_ten:
        n, v = top
        print n, v


if __name__ == '__main__':
    main()
