from bs4 import BeautifulSoup
import requests

def detect_updates():
  from secrets import URL,USERNAME,PASSWORD
  from ReadWriteS3 import readS3,writeS3

  res=requests.get(url=URL, auth=(USERNAME,PASSWORD))
  # print(res)

  soup=BeautifulSoup(res.text, "html.parser")
  # print(soup)

  new_elem=str(soup.select("li")[:5])

  try:
    old_elem=readS3()
  except IOError:
    old_elem=""

  if old_elem==new_elem:
    print("No change")
    return False
  else:
    writeS3(new_elem)
    print("There are some changes")
    return True

from slackPost import post

def main():
  if detect_updates():
    post()

if __name__ == "__main__":
  main()