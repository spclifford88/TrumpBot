import tweepy
import json

#///////////////////////////////////////////////////////////////
access_token = "3280145162-s5eyaIiSCfzMU46TyODBRqNxMln13XgxsNVfMTn"
access_token_secret = "Y3vtFJBhmK7Gj4RhPfCyXcmTqvaXorZavDiEJuAl4t6pX"
consumer_key = "u8iexDLmvil1b7pqcTmyDgArF"
consumer_secret = "46qEhTbOQRO36RXOGJe3iwxKJrEwRlkU6Kwzcd29VMC1xswpJJ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#///////////////////////////////////////////////////////////////
f = open("trump.json", "a+", encoding='utf-8')

def SaveToJson(text):
    tweet_dict = {"tweet_text" : text.text, "timestamp" : str(text.created_at)}
    tweet_json = json.dumps(tweet_dict)
    json.dump(tweet_dict, f, ensure_ascii=False, indent=4)
    f.write(',\n')
    return

#///////////////////////////////////////////////////////////////
class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if hasattr(status, 'retweeted_status'):
            return
        else:
            SaveToJson(status)
    def on_error(self, status_code):
        if status_code == 420:
            return False

stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=["realDonaldTrump"])

f.close()
print('done')
