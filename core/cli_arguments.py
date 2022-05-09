import argparse
from pathlib import Path

from core.data.config import PARENT_BASE, BASE_PATH


def create_parser():
    parser = argparse.ArgumentParser(description='Fortify Remote Client')
    parser.add_argument('-o', '--output', type=Path, default=BASE_PATH.joinpath('output.fvdl'),
                        help='output file')
    parser.add_argument('-t', '--target', type=Path, default=PARENT_BASE,
                        help=f'Path for analyzing. Default {PARENT_BASE}')
    parser.add_argument('-ht', '--host', type=str, default='localhost',
                        help='Server host. Default localhost')
    parser.add_argument('-p', '--port', type=int, default=33333,
                        help='Server port. Default 33333')
    return parser.parse_args()


cli_arguments = create_parser()
