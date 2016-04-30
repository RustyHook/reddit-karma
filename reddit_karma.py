import json
import urllib2

url = "https://reddit.com/u/howlingpotato.json"

data = json.load(urllib2.urlopen(url))

print data["data"]["children"][0]["data"]["score"]