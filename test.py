import re
import requests
import pandas
import matplotlib

f = open('bbs_urls.txt')
urls = f.read()
urls = urls.split('\n')
f.close()

s = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

for url in urls:
    try:
        r = s.get(url, headers = headers, timeout = 2)
        print(r, r.url)
    except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout):
        print('read time out:', r.url)
    except Exception as e:
        print(e.args, r.url)