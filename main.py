from bs4 import BeautifulSoup
import requests
import re
import datetime
import urllib.parse

class Page():
  def __init__(self, name, url, time):
    self.name = name
    self.url = url
    self.updated = time


def detect_updates():
  from secrets import ENDPOINT, USERNAME, PASSWORD, URL

  res=requests.get(url=ENDPOINT, auth=(USERNAME,PASSWORD))
  # print(res.status_code)

  updated = []
  if res.status_code == 200:
    soup=BeautifulSoup(res.text, "html.parser")
    # print(soup)

    for el in soup.select("li"):
      line = str(el)
      # print(line)
      name = re.search(r'">(.+)</a>', line).group(1)
      nums = re.findall('[0-9]+', re.search(r'</a> - (.+)</li>', line).group(1))
      nums = [int(i) for i in nums]
      time = datetime.datetime(*nums)
      url = URL+urllib.parse.quote(name)
      page = Page(name, url, time)
      if time < datetime.datetime(2022, 6, 10, 0, 0, 0):
        break
      updated.append(page)
      # print(name)
  return updated, res.status_code

  # try:
  #   old_elem=readS3()
  # except IOError:
  #   old_elem=""

  # if old_elem==new_elem:
  #   print("No change")
  # else:
  #   writeS3(new_elem)
  #   if res.status_code==200:
  #     print("There are some changes")
  #     post(res.status_code)
  #   else:
  #     print(f"Error: {res.status_code}")
  #     post(res.status_code)

# from slackPost import post
# import datetime

# def main(event, lambda_context):
def main():
  detect_updates()

if __name__ == "__main__":
  # main(event, lambda_context)
  main()