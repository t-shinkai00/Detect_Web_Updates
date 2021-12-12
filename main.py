from bs4 import BeautifulSoup
import requests

def detect_updates():
  from secrets import URL,USERNAME,PASSWORD
  from ReadWriteS3 import readS3,writeS3

  res=requests.get(url=URL, auth=(USERNAME,PASSWORD))
  print(res.status_code)

  soup=BeautifulSoup(res.text, "html.parser")
  # print(soup)

  new_elem=str(soup.select("li")[:5])

  try:
    old_elem=readS3()
  except IOError:
    old_elem=""

  if old_elem==new_elem:
    print("No change")
  else:
    writeS3(new_elem)
    if res.status_code==200:
      print("There are some changes")
      post(res.status_code)
    else:
      print(f"Error: {res.status_code}")
      post(res.status_code)

from slackPost import post

def main(event, lambda_context):
  detect_updates()

if __name__ == "__main__":
  main(event, lambda_context)