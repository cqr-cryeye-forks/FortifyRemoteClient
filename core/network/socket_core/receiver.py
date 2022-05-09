import json

from core.network.socket_core import Connection


def receive_data() -> dict:
    info = ''
    try:
        info = Connection.sock.recv(1024).decode('utf8')
        return json.loads(info)
    except json.decoder.JSONDecodeError as e:
        message = f'Error on decoding data: {info}'
        print(f'{message}\nError: {e}')
    except OSError as e:
        message = 'Connection error while receiving data'
        print(f'{message}: {e}')
    return {'status': 'error', 'result': message}
