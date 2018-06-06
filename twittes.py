import oauth2 as oauth
import json

CONSUMER_KEY = "Crf39vEDcFMCs9nZkTftsZrPb"
CONSUMER_SECRET = "OLzqvesVvxOLsuzWBiFpuFdl5R05ZDjB0NDkaTgDzCDBUoJEic"
ACCESS_KEY = "327636689-QIMd2glj8l42jcA0ZLts5oWMhSl4X4lFIV80I5xX"
ACCESS_SECRET = "PsnYQLHD1SXV4XplTFimTJYza4Zu0gVXI0nH6iklFPkOs"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

timeline_endpoint = "https://api.twitter.com/1.1/statuses/home_timeline.json"
response, data = client.request(timeline_endpoint)

tweets = json.loads(data)
for tweet in tweets:
    print tweet['text']
