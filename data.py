from nltk.tag import pos_tag
import sys
from textblob import TextBlob
import tweepy
import json
import re

consumer_key = 'WRxcgZHq8HOA9AiACeoz7pc61'
consumer_secret = 'IJnOARqL3baljF5VfMPB4Gy1GmxVLlSv6L4BgJoh3bVDslSQYL'

access_token = '32554005-yIgL0lbl0aWXyJ0E8q61zDF8BpOtVzWwRoZyCDm1n'
access_token_secret = 'PzknR8jcAmNgG35G0D99BH9qEJfF7n477AxK1kgFDnVWl'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

locale = ['at', 'in', 'on', 'from', 'to', 'toward', 'towards']

api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, count=5000,
                           lang="en",
                           #    since_id='2014-06-12'
                           geocode="37.0902,95.7129,500000000000km",
                           wait_on_rate_limit=True
                           ).items():
    # print('asdfasdf')
    if True:
        geo_taggable = {
            'has_proper_noun': 0,
            'has_link': 0,
            'has_hash_tag': 0,
            'has_locale': 0,
            'is_positive': 0,
            'can_be_tagged': 0,
            'is_tagged': 0,

        }
        # print(tweet.place, tweet.text, tweet.source, tweet._json)
        # break
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment.polarity)
        tagged_sent = pos_tag(tweet.text.split())
        propernouns = [word for word, pos in tagged_sent if pos == 'NNP']

        if analysis.sentiment.polarity > 0:
            geo_taggable["is_positive"] = 1

        if len(propernouns) > 0:
            geo_taggable["has_proper_noun"] = 1

        if bool(re.search('http', tweet.text)) or bool(re.search('bit', tweet.text)):
            geo_taggable["has_link"] = 1

        if bool(re.search('#', tweet.text)):
            geo_taggable["has_hash_tag"] = 1

        list_tweet_text = tweet.text.split()
        in_locale = [word for word in list_tweet_text if word in locale]
        if len(in_locale) > 0:
            geo_taggable["has_locale"] = 1

        total_checked = sum(list(geo_taggable.values()))
        percentage_liklyhood = ((total_checked/6)*100)

        geo_taggable['can_be_tagged'] = round(percentage_liklyhood, 2)

        if tweet.place:
            geo_taggable['is_tagged'] = 1

        values = list(geo_taggable.values())

        string_to_csv = f"{values[0]}, {values[1]}, {values[2]}, {values[3]}, {values[4]}, {values[5]}, {values[6]}"

        f = open('data.csv', 'a')
        f.write(string_to_csv + '\n\n')  # Give your csv text here.
        f.close()

        print(geo_taggable)

# [('Michael', 'NNP'), ('Jackson', 'NNP'), ('likes', 'VBZ'), ('to', 'TO'), ('eat', 'VB'), ('at', 'IN'), ('McDonalds', 'NNP')]

# ['Michael','Jackson', 'McDonalds']

# print('untagged ..............')
# print(tweet.created_at, tweet.text)


# class Data():

#     def livetwweets(self, topic):
#         pass


# public_tweets = api.search('Elon Musk')


# for tweet in public_tweets:

# searchTerm = input("Enter keyword/hastag to search about")
# print(searchTerm)
# no_searches = int(input("Enter number of tweets to analyze"))
# print(no_searches)
# longitude = float(input('Enter Longitude values here').strip())
# latitude = float(input('Enter Latitude values here').strip())
# radius = int(input('Enter radius values in km here').strip())

# geo = f"{longitude},{latitude},{radius}km"

# print(geo)
# print(type(geo))

# tweets = tweepy.Cursor(api.search, q=searchTerm,
#                        lang="English").items(no_searches)

# all_tweets = []
# non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)


# for tweet in tweepy.Cursor(api.search, q=searchTerm, geocode=geo).items(no_searches):
#     all_tweets.append(tweet.text.translate(non_bmp_map))

# all_tweets_text = ' '.join(all_tweets)
# print(all_tweets_text)

# blob = TextBlob(all_tweets_text)
# print(blob.sentiment.polarity)
# print(blob.sentiment.subjectivity)


# #    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'), tweet.user.id])
# #
# #positive = 0
# #negative = ArithmeticError
# #neutral = 0
# #polarity = 0
# '-33.602131,-70.576876,100000km'
# for tweet in tweets:
# print(tweet)
