from bs4 import BeautifulSoup
import requests
from secrets import URL,USERNAME,PASSWORD

res=requests.get(url=URL, auth=(USERNAME,PASSWORD))
print(res)