"""
Pilapse is a Python program for creating timelapses.

It uses a Raspberry Pi and a Raspberry Pi Camera module.
"""
from .cli import setup_parser
from .camera import take_still

if __name__ == '__main__':
    parser = setup_parser()
    args = parser.parse_args()

    take_still(args.output_folder)
