import requests, json
from secrets import WEBHOOK_URL

def post(status_code):
  if status_code ==200:
    data = json.dumps({
        'text': '研究室wikiの変更を検知しました。https://www2.nm.cs.uec.ac.jp/wiki/wiki.cgi?action=LIST',  #通知内容
        'link_names': 1,  #名前をリンク化
    })
  else:
    data = json.dumps({
        'text': f'{status_code}番のレスポンスが返りました。サーバーが落ちている可能性があります。',  #通知内容
        'link_names': 1,  #名前をリンク化
    })
  # print(data)
  requests.post(url=WEBHOOK_URL,data=data)