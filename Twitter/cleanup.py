import re

data = ""

with open('Tweets.txt', encoding="utf8") as f:
	for line in f.readlines():
		data += line
f.close()

text = re.sub(r'http\S+', '', data, flags=re.MULTILINE)

with open('cleaned_trump_v2.txt', encoding="utf8", mode='a') as w:
	w.write(text)
w.close()