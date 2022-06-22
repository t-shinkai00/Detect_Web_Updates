# Detect_Web_Updates

## 概要

- Web ページの変更をテキストベースで検知して変更があれば slack の Incoming Webhook を使って通知を送る機能を持っています。
- 私はこのプログラムを AWS Lambda に上げてクラウドで定期実行できるようにしています。また以前に実行した時間は Lambda の環境変数として扱っています。
