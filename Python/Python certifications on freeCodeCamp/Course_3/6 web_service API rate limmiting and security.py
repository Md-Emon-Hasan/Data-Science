# web service api rate limiting and security
import urllib.request, urllib.parse, urllib.error
import twurl
import json

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
while True:
    print('')
    acct = input("enter twitter account:")
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    header = dict(connection.getheaders())
    print("Remaining", header['x-rate-limit-remaining'])
    js = json.loads(data)
    print(json.dumps(js, indent=4))
    
    for u in js['users']:
        print(u['screen_name'])
        s = u['status']['text']
        print(' ',s[:50])