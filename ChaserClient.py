import ipaddress
import sys
from Connection import Connection

TURN_START = '@'
TURN_END = '#'
GAME_END = '0'


class ChaserClient:
    def __init__(self, host: str, port: str, name: str) -> None:

        if not self._check_ip_addr_format(host):
            sys._exit(1)

        self.host = host
        self.port = port
        self.name = name
        self.connection = None

    def connect(self):
        self.connection = Connection(self.host, self.port)
        self.connection.connect()
        self._send_name()

    def close(self):
        self.connection.close()

    def _check_ip_addr_format(self, ip_address: str) -> bool:
        try:
            ipaddress.ip_address(ip_address)
        except ValueError as e:
            print(f"IPアドレスの形式が違います。: {e}")
            return False
        except Exception as e:
            print(e)
        else:
            return True

    def _send_command(self, command: str):
        try:
            self.connection.send(command + "\r\n")
        except Exception as e:
            print(f"コマンドの送信にエラーが発生しました。：{e}")

    def _send_name(self):
        try:
            self.connection.send(self.name)
        except Exception as e:
            print(f"チーム名の送信に失敗しました。 :{e}")

    def receive(self):
        response = self.connection.recv()
        control_code = response[0]
        if control_code == TURN_START or control_code == GAME_END:
            return control_code, None
        else:
            return control_code, list(response[1:10])

    def get_ready(self):
        self._send_command("gr")
        return self.receive()

    def turn_end(self):
        self._send_command(TURN_END)

    def walk_right(self):
        self._send_command("wr")
        return self.receive()

    def walk_left(self):
        self._send_command("wl")
        return self.receive()

    def walk_up(self):
        self._send_command("wu")
        return self.receive()

    def walk_down(self):
        self._send_command("wd")
        return self.receive()

    def look_right(self):
        self._send_command("lr")
        return self.receive()

    def look_left(self):
        self._send_command("ll")
        return self.receive()

    def look_up(self):
        self._send_command("lu")
        return self.receive()

    def look_down(self):
        self._send_command("ld")
        return self.receive()

    def search_right(self):
        self._send_command("sr")
        return self.receive()

    def search_left(self):
        self._send_command("sl")
        return self.receive()

    def search_up(self):
        self._send_command("su")
        return self.receive()

    def search_down(self):
        self._send_command("sd")
        return self.receive()

    def put_right(self):
        self._send_command("pr")
        return self.receive()

    def put_left(self):
        self._send_command("pl")
        return self.receive()

    def put_up(self):
        self._send_command("pu")
        return self.receive()

    def put_down(self):
        self._send_command("pd")
        return self.receive()
