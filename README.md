# chaser-python-client

`U-16プログラミングコンテスト`で利用される`CHaser`のクライアントとライブラリのサンプルコードです。
Python3及びPythonに標準で搭載しているライブラリで利用可能です。

CHaserサーバとのsocket通信及び、プログラムの終了処理はライブラリで実装しているため、
利用時はPythonを用いたクライアントのアルゴリズムに集中することができます。

本リポジトリには2種類のライブラリと、それを用いた2種類のクライアントのサンプルコードを格納しています。
- ChaserClient.py
  - サーバへの接続手順をユーザ側で実装
  - ゲームの継続性判定用の制御コードをユーザ側に返す
- ChaserSimpleClient.py
  - サーバへの接続手順をユーザ側で実装しなくてよい
  - ゲームの接続正判定用コードをユーザ側に返さない
    - 広く使われているC#のライブラリと同様の動作

CHaserのクライアント開発には`ChaserSimpleClient.py`を利用したほうがより簡単に実装できます。
以下は`ChaserSimpleClient.py`を用いた例を紹介します。

## 使い方
sample_SimpleClient.pyを参照してください。
### ディレクトリ構成
プログラムを作成するときには、以下の構成で利用してください。

```
.
├── client
│   ├── ChaserClient.py
│   └── ChaserSimpleClient.py
├── main.py (作成するプログラム本体)
└── utils
    └── Connection.py
```

### ターン内での処理順序
- 各ターンごとにget_ready() → 行動関数 → get_ready() → 行動関数 → ・・・の順で処理を行います。

### クライアントの行動を決める関数
- 行動関数は「行動_方向()」の形式となっています。

|行動|
|---|
|walk|
|look|
|search|
|put|

|方向|
|---|
|right|
|up|
|left|
|down|

例えばこのように指定します。
- 左にsearchを行うときは、`search_left()`
- 右に1マス移動するときは、`walk_right()`

#### 行動後の戻り値
各行動後には、自分の周り9マスのマップ情報がlist形式で返ります。

例えばこのようなマップの場合には、

`[0,2,2,0,0,3,1,0,0]`というlistが返ります。

``` マップの状態
[ ][x][x]
[ ][C][♡]
[H][ ][ ]
```

## 動作環境
以下の環境で動作を確認しています。
- macOS Monterey 12.5
- Python3.10.1