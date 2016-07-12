"""Handles the Command Line Interface part of Pilapse."""

import argparse


DESCRIPTION = ("Takes stills using a connected Raspberry Pi Camera")


def setup_parser():
    """Set up an argparse parser and return it."""
    parser = argparse.ArgumentParser(prog="pilapse",
                                     description=DESCRIPTION)

    parser.add_argument("output_folder",
                        help="The folder in which stills are saved.")

    parser.add_argument("--name", "-n",
                        dest="name",
                        help=("Base name to use for stills."
                              " Datetime info is added automatically. "
                              "Default: 'pilapse'"),
                        default="pilapse")

    parser.add_argument("--iso", "-i",
                        dest="iso",
                        help=("Sets the ISO value of the camera. "
                              "Guide: 100-200 for daytime, "
                              "400-800 for nighttime"),
                        type=int,
                        default=100)

    return parser
