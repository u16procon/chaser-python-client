import socket

BUFFER_SIZE = 4096


class Connection:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.socket = None

    def connect(self) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def close(self) -> None:
        self.socket.close()

    def send(self, command: str):
        command = command.encode('utf-8')
        return self.socket.send(command)

    def recv(self) -> str:
        return self.socket.recv(BUFFER_SIZE).decode('utf-8')
