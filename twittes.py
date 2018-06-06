import json
import oauth2 # https://raw.github.com/brosner/python-oauth2/master/oauth2/__init__.py
from pprint import pprint
import urllib2


stream_url = "https://stream.twitter.com/1/statuses/filter.json"

filename = "ids.txt"

consumer_key = "Crf39vEDcFMCs9nZkTftsZrPb"
consumer_secret = "OLzqvesVvxOLsuzWBiFpuFdl5R05ZDjB0NDkaTgDzCDBUoJEic"
access_token = "327636689-QIMd2glj8l42jcA0ZLts5oWMhSl4X4lFIV80I5xX"
access_token_secret = "PsnYQLHD1SXV4XplTFimTJYza4Zu0gVXI0nH6iklFPkOs"


def main():
    user_ids = list()
    with open(filename) as f:
        for line in f:
            user_id = line.strip()
            assert int(user_id)
            user_ids.append(user_id)
    print "Have %d user ids" % len(user_ids)

    consumer = oauth2.Consumer(key=consumer_key, secret=consumer_secret)
    token = oauth2.Token(key=access_token, secret=access_token_secret)
    client = oauth2.Client(consumer, token)

    # not using client.request() - it would block forever...
    # maybe there is better way, but this works

    url = stream_url
    headers = {}
    parameters = {"follow": ",".join(user_ids[:5000])}

    req = oauth2.Request.from_consumer_and_token(
        client.consumer, token=client.token,
        http_method="POST", http_url=url, parameters=parameters)

    req.sign_request(client.method, client.consumer, client.token)

    # ensure we always send Authorization
    headers.update(req.to_header())

    body = req.encode_postdata(req.get_nonoauth_parameters())
    headers['Content-Type'] = 'application/x-www-form-urlencoded'

    print "%s %s... %s" % (url, repr(body)[:100], headers)
    req = urllib2.Request(url, body, headers=headers)
    try:
        f = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        data = e.fp.read(1024)
        raise Exception("Caught %r %s" % (e, data))
    print f
    print "---------------------------------------"
    for line in f:
        d = json.loads(line)
        #pprint(d)
        #print "---------------------------------------"
        try:
            print "%s: %s" % (d["user"]["name"], d["text"])
        except:
            print d.get("id")


if __name__ == "__main__":
    main()
