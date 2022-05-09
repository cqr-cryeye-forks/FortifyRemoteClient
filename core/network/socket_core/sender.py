import json

from core.data.classes import CommandStatus
from core.network.socket_core import connect, Connection


def send_to_server(command: str = '',
                   status: str = CommandStatus.INFO.value,
                   message: str = '') -> None:
    data = {
        'command': command,
        'status': status,
        'message': message,
    }
    try:
        info = json.dumps(data).encode('utf8')
        Connection.sock.sendall(info)
    except json.decoder.JSONDecodeError as e:
        print(f'Encode error: {e}')
    except OSError as e:
        print(f'Connection error: {e}')
        connect()
