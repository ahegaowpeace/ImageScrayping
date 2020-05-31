# nhentai_scrayping (/lnkpg_folk)
## useage
```
$ python3.6 image.py アンスリウム202012 https://www.google.co.jp/hoge/moge 499
```
## 概要
- nhentai用スクリプト
- ウィザード形式ではなく引数形式にする事でクリップボードから連続でスクリプトを実行出来る
## 途中スクリプト (totyu_image.py)
- 変数numには成功した最後のページ数をセット
  - (46行) num = 131
- rangeの初期値には再取得したい開始ページ数をセット
  - (59行) for nm in range(132,int(n) + 1):
- 同名のディレクトリがあると次のスクレイピングが実行出来ない
  - 途中まで取得出来たものはtmpディレクトリへ避難
