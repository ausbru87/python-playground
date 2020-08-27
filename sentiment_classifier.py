
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def read_csv(file_name):
    # takes a str as the filename input
    return file_name

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

# list of negative words to use
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(in_str):
    # takes a string, and returns a clean string with no punctuation
    for char in in_str:
        if char in punctuation_chars:
            in_str = in_str.replace(char, '')
    return in_str

def get_pos(in_str):
    # takes a string, cleans it, and returns the number of 
    # that are considered positive
    #cln_str = strip_punctuation(in_str)
    cnt = 0
    for word in in_str.lower().split():
        if word in positive_words:
            cnt += 1
    return cnt

def get_neg(in_str):
    # takes a string, cleans it, and returns the number of 
    # that are considered negative
    #cln_str = strip_punctuation(in_str)
    cnt = 0
    for word in in_str.lower().split():
        if word in negative_words:
            cnt += 1
    return cnt

def get_net(in_str):
    # returns sentiment metrics in list of strings
    cln_str = strip_punctuation(in_str)
    pos_ct = get_pos(cln_str)
    neg_ct = get_neg(cln_str)
    net_ct = pos_ct - neg_ct
    return [str(pos_ct), str(neg_ct), str(net_ct)]

def format_out(in_lst):
    # pass in list of items, returns string of items in csv format.
    return ','.join(in_lst)

def process_tweet(in_line):
    # takes in lst of items from line of tweet data and outputs a list of 
    # in order of header items [num of retweets, num replies, pos score, neg score, net score]
    tweet_metrics = in_line.strip().split(',')[1:]
    tweet_text = in_line.strip().split(',')[0]
    sent_metrics = get_net(tweet_text)
    return format_out(tweet_metrics + sent_metrics)
    

header = "Number of Retweets,Number of Replies,Positive Score,Negative Score,Net Score"
with open('resulting_data.csv', 'w') as results:
    results.write(header)
    results.write('\n')
    with open('twitter_data.csv', 'r') as tw_data:
        lines = tw_data.readlines()
        for row in lines[1:]:
            results.write(process_tweet(row))
            results.write('\n')
