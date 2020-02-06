import json
import nltk

data = []
with open('TrumpBot/TweetHistory/trump.json') as json_file:
    data = json.load(json_file)

for t in data['trump']:
	tokens = [t for t in t['tweet_text'].split()]
	#print(t['tweet_text'])

#print(tokens)

from nltk.corpus import stopwords
sr = stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
	if token in stopwords.words('english'):
		clean_tokens.remove(token) 

freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
	print(str(key) + ':' + str(val))

freq.plot(30, cumulative=False)