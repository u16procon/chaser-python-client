from client.ChaserSimpleClient import ChaserSimpleClient


def main():
    # ChaserSimpleClient("CHaserサーバが動いているマシンのIPアドレス", "CHaserサーバのポート番号", "チームや自身の名前")
    client = ChaserSimpleClient("192.168.xx.x", 2009, "test")

    while True:
        # マップ情報を記載する空listを作成
        map_info = []

        # 準備ができたらget_ready()を行う
        map_info = client.get_ready()

        # map_infoの内容を表示する
        print(map_info)

        # 自身の左をサーチする
        map_info = client.search_left()

        # map_infoの内容を表示する
        print(map_info)

    # ゲームを終了する
    client.close()


if __name__ == "__main__":
    main()
