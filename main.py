class Page():
  def __init__(self, name, url, time):
    self.name = name
    self.url = url
    self.updated = time

from bs4 import BeautifulSoup
import requests
import re
import datetime
import urllib.parse
# import os
def detect_updates(newDate):
  from secrets import ENDPOINT, USERNAME, PASSWORD, URL
  oldDate = datetime.datetime.strptime("2022-6-20 0:0:0", "%Y-%m-%d %H:%M:%S")
  # oldDate = datetime.datetime.strptime(os.environ["Date"], "%Y-%m-%d %H:%M:%S")

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


import requests, json
from secrets import WEBHOOK_URL
def post(updated, status):
  if status != 200:
    print(f"Error: {status}")
    data = json.dumps(
      {
        'text': f'wikiから{status}番のレスポンスが返りました。サーバーが落ちている可能性があります。',  #通知内容
        'link_names': 1,  #名前をリンク化
      }
    )
  else:
    print("There are some changes")
    contents = "研究室wikiの変更を検知しました。\n"  #通知内容
    size = len(updated)
    for i, el in enumerate(updated):
      if i != size - 1:
        contents += f"• <{el.url}|{el.name}> ({el.updated})\n"
    print(contents)
    data = json.dumps(
    {
      'link_names': 1,  #名前をリンク化
      "blocks": [
        {
          "type": "section",
          "text": {
            "type": "mrkdwn",
            "text": contents,
          }
        },
      ]
    }
    )
  requests.post(url=WEBHOOK_URL,data=data)


# def main(event, lambda_context):
def main():
  updated, status = detect_updates()
  if status == 200 and len(updated) == 0: print("No change.")
  else: post(updated, status)

if __name__ == "__main__":
  # main(event, lambda_context)
  main()