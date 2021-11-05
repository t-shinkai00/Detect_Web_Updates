import requests, json
from secrets import WEBHOOK_URL

def post():
  data = json.dumps({
      'text': '研究室wikiの変更を検知しました。https://www2.nm.cs.uec.ac.jp/wiki/wiki.cgi?action=LIST',  #通知内容
      'link_names': 1,  #名前をリンク化
  })
  requests.post(url=WEBHOOK_URL,data=data)