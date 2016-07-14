"""
Pilapse is a Python program for creating timelapses.

It uses a Raspberry Pi and a Raspberry Pi Camera module.
"""

__version__ = (0, 0, 1)


from .cli import setup_parser, check_args  # noqa
from .camera import take_still  # noqa


if __name__ == '__main__':
    parser = setup_parser()
    args = parser.parse_args()
    check_args(args)

    take_still(args.output_folder)
