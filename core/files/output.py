import json
from pathlib import Path

from dict2xml import dict2xml


def save_result(result: bytes, output_path: Path):
    if output_path.suffix == '.json':
        result = json.loads(result)
        with open(output_path, 'w') as file:
            json.dump(result, file, indent=2)
            file.close()
    else:
        with open(output_path, 'wb') as file:
            if output_path.suffix in ['.xml', 'fvdl']:
                result = dict2xml(result)
            file.write(result)
            file.close()
    print(f'Data saved to {output_path.absolute()}')
