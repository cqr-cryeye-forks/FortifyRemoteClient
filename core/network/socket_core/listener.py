import json
import os
import shutil
from time import sleep

from core.data.classes import ServerCommands, CommandStatus
from core.network.socket_core import send_to_server, connect, Connection
from core import cli_arguments, print_result_message
from core.data.config import BASE_PATH
from core.files.output import save_result
from core.network.socket_core.results_getter import wait_and_receive_data

BYTEORDER_LENGTH = 8


def socket_listener():
    connect()
    sleep(3)
    if Connection.connected is True:

        # [SEND-FILE] - [BEGIN]
        send_to_server(command=ServerCommands.GET_FILE.value)
        temp_data = False
        if cli_arguments.target.suffix == '.zip':
            target_archive = cli_arguments.target
        else:
            shutil.make_archive(BASE_PATH.joinpath('target'), 'zip', cli_arguments.target)
            target_archive = BASE_PATH.joinpath('target.zip')
            temp_data = True

        file_size = os.path.getsize(target_archive)
        file_size_in_bytes = file_size.to_bytes(BYTEORDER_LENGTH, 'big')
        print("Sending file size...")
        Connection.sock.send(file_size_in_bytes)
        msg = Connection.sock.recv(1024).decode('utf8')
        print(f"[SERVER]: {msg}")
        print("Sending file data...")

        # with open(target_archive, 'rb') as file:
        #     Connection.sock.sendfile(file)
        with open(target_archive, 'rb') as f1:
            Connection.sock.send(f1.read())
        msg = Connection.sock.recv(1024).decode('utf8')
        print(f"SERVER: {msg}")
        # [SEND-FILE] - [END]

        send_to_server(command=ServerCommands.RUN_SCAN.value, message='clean_results')
        data = wait_and_receive_data()
        print_result_message(data)
        file_size = int(data.get('length', 1024))
        if data.get('status') != CommandStatus.ERROR.value:
            send_to_server(command=ServerCommands.GET_RESULT.value)
            print("Receiving results...")
            packet = b""
            while len(packet) < file_size:
                if (file_size - len(packet)) > 1024:  # if remaining bytes are more than the defined chunk size
                    buffer = Connection.sock.recv(1024)
                else:
                    buffer = Connection.sock.recv(file_size - len(packet))  # read remaining number of bytes
                if not buffer:
                    raise Exception("Incomplete file received")
                packet += buffer
            print('Result received')
            save_result(result=packet, output_path=cli_arguments.output)
        if temp_data:
            shutil.rmtree(target_archive, ignore_errors=True)
            print(f'Temp data removed: {target_archive}')
    else:
        error = {'type': 'Connection error', 'message': 'No connection with server'}
        results = json.dumps({'errors': [error]})
        save_result(result=results, output_path=cli_arguments.output)
        print('No connection')
