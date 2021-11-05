# Detect_Web_Updates

## 概要

- Web ページの変更をテキストベースで検知して変更があれば Slack の Incoming Webhook を使って通知を送る機能を持っています。
- 私は所属する研究室のサイトの更新があるかどうかを検知するためにこれを作成したので他のサイトでこれを動かしたい場合は色々変更する箇所があると思いますのでご容赦ください。

## 簡単に試したい場合

- slack の Incoming Webhook を作成し Webhook URL をコピー
- `secrets.py`を作成して変数 URL, USERNAME, PASSWORD, WEBHOOK_URL を記載する
- 検知したいサイトに基本認証がない場合`main.py`の 7 行目から`auth=(USERNAME,PASSWORD)`を省く
- `main.py`の 13 行目を変更して検知したい対象を書く
- `pip install -r requirements.txt`を実行してモジュールのインストールを行う
- `python3 main.py`を実行
