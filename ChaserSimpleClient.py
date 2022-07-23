import sys
from ChaserClient import ChaserClient

TURN_END = '0'


class ChaserSimpleClient():
    def __init__(self, host: str, port: str, name: str):
        self.client = ChaserClient(host, port, name)
        self.client.connect()

    def close(self):
        self.client.close()

    def get_ready(self):
        control_code, map_info = self.client.receive()
        if control_code == TURN_END:
            self.client.close()
            sys.exit(1)
        control_code, map_info = self.client.get_ready()
        if control_code == TURN_END:
            self.client.close()
            sys.exit(1)
        return map_info

    def walk_right(self):
        self.client._send_command("wr")
        control_code, map_info = self.client.receive()
        self.client.turn_end()
        return map_info

    def walk_left(self):
        self.client._send_command("wl")
        control_core, map_info = self.client.receive()
        self.client.turn_end()
        return map_info

    def walk_up(self):
        self.client._send_command("wu")
        control_code, map_info = self.client.receive()
        self.client.turn_end()
        return map_info

    def walk_down(self):
        self.client._send_command("wd")
        control_code, map_info = self.client.receive()
        self.client.turn_end()
        return map_info

    def look_right(self):
        self.client._send_command("lr")
        control_code, map_info = self.client.receive()
        self.client.turn_end()
        return map_info

    def look_left(self):
        self.client._send_command("ll")
        control_code, map_info = self.client.receive()
        self.client.turn_end()
        return map_info

    def look_up(self):
        self.client._send_command("lu")
        control_code, map_info = self.client.receive()
        self.client.turn_end()
        return map_info

    def look_down(self):
        self.client._send_command("ld")
        control_code, map_info = self.client.receive()
        self.client.turn_end()
        return map_info

    def search_right(self):
        self.client._send_command("sr")
        control_code, map_info = self.client.receive()
        self.client.turn_end()
        return map_info

    def search_left(self):
        self.client._send_command("sl")
        control_code, map_info = self.client.receive()
        self.client.turn_end()
        return map_info

    def search_up(self):
        self.client._send_command("su")
        control_code, map_info = self.client.receive()
        self.client.turn_end()
        return map_info

    def search_down(self):
        self.client._send_command("sd")
        control_code, map_info = self.client.receive()
        self.client.turn_end()
        return map_info

    def put_right(self):
        self.client._send_command("pr")
        control_code, map_info = self.client.receive()
        self.client.turn_end()
        return map_info

    def put_left(self):
        self.client._send_command("pl")
        control_code, map_info = self.client.receive()
        self.client.turn_end()
        return map_info

    def put_up(self):
        self.client._send_command("pu")
        control_code, map_info = self.client.receive()
        self.client.turn_end()
        return map_info

    def put_down(self):
        self.client._send_command("pd")
        control_code, map_info = self.client.receive()
        self.client.turn_end()
        return map_info
