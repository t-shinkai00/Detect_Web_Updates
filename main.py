from bs4 import BeautifulSoup
import requests
from secrets import URL,USERNAME,PASSWORD

res=requests.get(url=URL, auth=(USERNAME,PASSWORD))
# print(res)

soup=BeautifulSoup(res.text, "html.parser")
# print(soup)

new_elem=str(soup.select(".body"))