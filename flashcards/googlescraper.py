import urllib
import json
def google_image(x):
        search = x.split()
        search = '%20'.join(map(str, search))
        url = 'http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=%s&safe=off' % search
        search_results = urllib.urlopen(url)
        js = json.loads(search_results.read().decode('utf-8'))
        results = js['responseData']['results']
        for i in results: rest = i['unescapedUrl']
        return rest
