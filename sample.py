from ChaserClient import ChaserClient


def main():
    client = ChaserClient("192.168.xx.x", 2009, "test")
    client.connect()

    while True:
        control_code, map_info = client.receive()
        if control_code == 0:
            break

        control_code, map_info = client.get_ready()
        control_code, map_info = client.search_left()
        print(map_info)
        client.turn_end()

        control_code, map_info = client.receive()
        control_code, map_info = client.get_ready()
        print(map_info)
        if map_info[7] != 2:
            control_code, map_info = client.walk_down()
        else:
            control_code, map_info = client.put_up()
        client.turn_end()

        control_code, map_info = client.receive()
        control_code, map_info = client.get_ready()
        control_code, map_info = client.look_up()
        client.turn_end()

        control_code, map_info = client.receive()
        control_code, map_info = client.get_ready()
        control_code, map_info = client.put_right()
        client.turn_end()


if __name__ == "__main__":
    main()
