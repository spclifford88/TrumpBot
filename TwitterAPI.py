import tweepy
import time
import json
#///////////////////////////////////////////////////////////////
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#///////////////////////////////////////////////////////////////
#user = api.get_user(screen_name = 'realDonaldTrump')
#print(user.id)

#///////////////////////////////////////////////////////////////
#user = api.get_user(25073877)
#print(user.screen_name)

#///////////////////////////////////////////////////////////////
#try:
#    for tweet in tweepy.Cursor(api.user_timeline, screen_name="realDonaldTrump", exclude_replies=True).items():
#                    print(tweet)
#except tweepy.TweepError:
#    time.sleep(60)

#///////////////////////////////////////////////////////////////
f = open('trump.json', 'a+', encoding='utf-8')

try:
    for tweet in tweepy.Cursor(api.user_timeline, screen_name="realDonaldTrump", include_rts=False, exclude_replies=True, count = 200, tweet_mode="extended").items():
        tweet_text = tweet.full_text
        time = tweet.created_at
        tweet_dict = {"tweet_text" : tweet_text, "timestamp" : str(time)}
        tweet_json = json.dumps(tweet_dict)
        json.dump(tweet_dict, f, ensure_ascii=False, indent=4)
        f.write(',\n')
except tweepy.TweepError:
    time.sleep(60)

f.close()
print('done')
