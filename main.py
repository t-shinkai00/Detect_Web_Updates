from bs4 import BeautifulSoup
import requests
from secrets import URL,USERNAME,PASSWORD

res=requests.get(url=URL, auth=(USERNAME,PASSWORD))
# print(res)

soup=BeautifulSoup(res.text, "html.parser")
# print(soup)

new_elem=str(soup.select("li")[:5])

try:
  with open("old_elem.txt") as f:
    old_elem=f.read()
except IOError:
  old_elem=""

if old_elem==new_elem:
  print("No change")
else:
  with open("old_elem.txt", "w") as f:
    f.write(new_elem)
  print("There are some change")