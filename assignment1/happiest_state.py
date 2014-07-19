import sys
import json
import operator

states = {
        'Alaska' : 'AK',
        'Alabama' : 'AL',
        'Arkansas' : 'AR',
        'American Samoa' : 'AS',
        'Arizona' : 'AZ',
        'California' : 'CA',
        'Colorado' : 'CO',
        'Connecticut' : 'CT',
        'District of Columbia' : 'DC',
        'Delaware' : 'DE',
        'Florida' : 'FL',
        'Georgia' : 'GA',
        'Guam' : 'GU',
        'Hawaii' : 'HI',
        'Iowa' : 'IA',
        'Idaho' : 'ID',
        'Illinois' : 'IL',
        'Indiana' : 'IN',
        'Kansas' : 'KS',
        'Kentucky' : 'KY',
        'Louisiana' : 'LA',
        'Massachusetts' : 'MA',
        'Maryland' : 'MD',
        'Maine' : 'ME',
        'Michigan' : 'MI',
        'Minnesota' : 'MN',
        'Missouri' : 'MO',
        'Northern Mariana Islands' : 'MP',
        'Mississippi' : 'MS',
        'Montana' : 'MT',
        'National' : 'NA',
        'North Carolina' : 'NC',
        'North Dakota' : 'ND',
        'Nebraska' : 'NE',
        'New Hampshire' : 'NH',
        'New Jersey' : 'NJ',
        'New Mexico' : 'NM',
        'Nevada' : 'NV',
        'New York' : 'NY',
        'Ohio' : 'OH',
        'Oklahoma' : 'OK',
        'Oregon' : 'OR',
        'Pennsylvania' : 'PA',
        'Puerto Rico' : 'PR',
        'Rhode Island' : 'RI',
        'South Carolina' : 'SC',
        'South Dakota' : 'SD',
        'Tennessee' : 'TN',
        'Texas' : 'TX',
        'Utah' : 'UT',
        'Virginia' : 'VA',
        'Virgin Islands' : 'VI',
        'Vermont' : 'VT',
        'Washington' : 'WA',
        'Wisconsin' : 'WI',
        'West Virginia' : 'WV',
        'Wyoming' : 'WY'
}


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # terms sentiment score
    locations = {}  # locations and their list of scores

    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    for line in tweet_file:
        line = json.loads(line)
        if 'lang' in line:  # excluding all but tweet messages
            if line['place'] and line['lang'] == 'en':  # excluding non-english tweets
                if line['place']['country_code'] == 'US':
                    place = line['place']['full_name'].split(', ')

                    text = line['text'].lower().split()
                    score = 0
                    for term in text:
                        if term in scores:
                            score = score + scores[term]

                    if len(place[1]) == 2:
                        p = place[1]
                    elif place[1] == 'USA':
                        p = states[place[0]]
                    if place[1] in locations:
                        locations[p].append(score)
                    else:
                        locations[p] = [score]

    st_sc = {k: sum(v)/len(v) for k, v in locations.items()}
    sorted_x = sorted(st_sc.iteritems(), key=operator.itemgetter(1), reverse=True)
    print sorted_x[0][0]


if __name__ == '__main__':
    main()
