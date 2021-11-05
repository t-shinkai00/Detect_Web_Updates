from bs4 import BeautifulSoup
import requests

def detect_updates():
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
    return False
  else:
    with open("old_elem.txt", "w") as f:
      f.write(new_elem)
    print("There are some changes")
    return True

from slackPost import post

def main():
  if detect_updates():
    post(1)
  else:
    post(0)

if __name__ == "__main__":
  main()