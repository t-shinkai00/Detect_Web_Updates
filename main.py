from bs4 import BeautifulSoup
import requests

url = 'https://www2.nm.cs.uec.ac.jp/wiki/wiki.cgi?action=LIST'
res=requests.get(url)
print(res)