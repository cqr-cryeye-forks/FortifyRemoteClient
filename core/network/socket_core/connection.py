import socket

from core import cli_arguments


class SocketInfo:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected = False

    def __init__(self):
        self.connected = False


Connection = SocketInfo()


def connect():
    try:
        reconnect_socket()
    except Exception as e:
        Connection.connected = False
        print(f'Server not responding: {e}')


def reconnect_socket():
    Connection.sock.close()

    print(f'Connecting to {cli_arguments.host}:{cli_arguments.port}...')
    Connection.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Connection.sock.connect((cli_arguments.host, cli_arguments.port))
    Connection.connected = True
    print('Connected to the server')
