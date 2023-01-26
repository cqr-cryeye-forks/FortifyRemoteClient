from core.network.socket_core import receive_data


def wait_and_receive_data() -> dict:
    results = {}
    scan_is_finished = False

    while not scan_is_finished:
        data = receive_data()
        scan_status = data.get('status', 'Unknown')
        print(f"scan status: {scan_status}")
        if scan_status == 'error':
            scan_is_finished = True
            results = {'errors': ['Connection lost or error during scan']}
        if data.get('is_finished', False):
            print(f'Scan finished! status: {scan_status}')
            scan_is_finished = True
            results = data

    return results
