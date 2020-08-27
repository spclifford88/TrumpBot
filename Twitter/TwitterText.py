from twython import Twython
import PersonalOAuth as key
import TrumpML as trump
import numpy as np
import torch

message = trump.trumpTrain(False)

twitter = Twython(key.consumer_key, key.consumer_secret, key.access_token, key.access_token_secret)

twitter.update_status(status=message)
print("Tweeted: %s" % message)