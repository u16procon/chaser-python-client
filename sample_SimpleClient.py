from ChaserSimpleClient import ChaserSimpleClient


def main():
    client = ChaserSimpleClient("192.168.xx.x", 2009, "test")

    while True:
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
