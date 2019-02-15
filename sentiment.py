# import tweepy
# from textblob import TextBlob
# import json
# import sys


# consumer_key = 'WRxcgZHq8HOA9AiACeoz7pc61'
# consumer_secret = 'IJnOARqL3baljF5VfMPB4Gy1GmxVLlSv6L4BgJoh3bVDslSQYL'

# access_token = '32554005-yIgL0lbl0aWXyJ0E8q61zDF8BpOtVzWwRoZyCDm1n'
# access_token_secret = 'PzknR8jcAmNgG35G0D99BH9qEJfF7n477AxK1kgFDnVWl'

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# #public_tweets = api.search('Elon Musk')

# # for tweet in public_tweets:
# #   analysis = TextBlob(tweet.text)
# #   print(analysis.sentiment.polarity)

# api = tweepy.API(auth)

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


# ##    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'), tweet.user.id])
# ##
# ##positive = 0
# ##negative = ArithmeticError
# ##neutral = 0
# ##polarity = 0
# # '-33.602131,-70.576876,100000km'
# # for tweet in tweets:
# # print(tweet)
