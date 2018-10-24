import urllib.parse
import urllib.request
import json

baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = "select wind from weather.forecast where woeid=2460286"
yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
result = urllib.request.urlopen(yql_url).read()
data = json.loads(result)
print data['query']['results']