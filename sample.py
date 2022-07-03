from ChaserClient import ChaserClient


def main():
    client = ChaserClient("192.168.xx.x", 2009, "test")
    client.connect()

    while True:
        # 制御コードとマップ情報を得る
        control_code, map_info = client.receive()
        # 制御コードが0の場合ループを抜ける
        if control_code == 0:
            break

        # 準備ができたらget_ready()を行う
        control_code, map_info = client.get_ready()
        # 自身の左をサーチする
        control_code, map_info = client.search_left()
        # map情報をコンソールに表示する
        print(map_info)
        # ターンを終了する
        client.turn_end()

    client.close()


if __name__ == "__main__":
    main()
